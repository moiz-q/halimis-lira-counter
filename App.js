import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Image,
  ScrollView,
  ActivityIndicator,
  Alert,
  Platform,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import * as ImagePicker from 'expo-image-picker';
import { CameraView, useCameraPermissions } from 'expo-camera';
import { LinearGradient } from 'expo-linear-gradient';

// IMPORTANT: Update this URL to match your API server
// Replace 'localhost' with your computer's IP address
// Find your IP: Windows (run 'ipconfig'), Mac/Linux (run 'ifconfig')
// Example: const API_URL = 'http://192.168.1.100:8080';
const API_URL = 'http://10.110.130.179:8080'; // ⚠️ CHANGE THIS to your computer's IP!

export default function App() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showCamera, setShowCamera] = useState(false);
  const [permission, requestPermission] = useCameraPermissions();

  const pickImage = async () => {
    try {
      const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
      if (status !== 'granted') {
        Alert.alert('Permission needed', 'Sorry, we need camera roll permissions!');
        return;
      }

      const result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        allowsEditing: false, // No cropping - process full image
        quality: 0.8,
        base64: true, // Get base64 directly
      });

      if (!result.canceled && result.assets[0]) {
        setImage(result.assets[0].uri);
        setResult(null);
        // Use base64 directly if available, otherwise process URI
        if (result.assets[0].base64) {
          processImage(`data:image/jpeg;base64,${result.assets[0].base64}`);
        } else {
          processImage(result.assets[0].uri);
        }
      }
    } catch (error) {
      console.error('Error picking image:', error);
      Alert.alert('Error', 'Failed to pick image');
    }
  };

  const takePhoto = async () => {
    try {
      if (!permission) {
        // Permission is still loading
        return;
      }
      
      if (!permission.granted) {
        const result = await requestPermission();
        if (!result.granted) {
          Alert.alert('Permission needed', 'Sorry, we need camera permissions!');
          return;
        }
      }

      setShowCamera(true);
    } catch (error) {
      console.error('Error opening camera:', error);
      Alert.alert('Error', 'Failed to open camera');
    }
  };

  const handleCameraCapture = async (uri) => {
    setShowCamera(false);
    setImage(uri);
    setResult(null);
    // Camera returns URI, we'll process it
    processImage(uri);
  };

  const processImage = async (imageUri) => {
    setLoading(true);
    try {
      // Convert image to base64 using fetch
      // For React Native, we need to handle the URI differently
      let base64data;
      
      // Check if it's already a base64 data URI
      if (imageUri.startsWith('data:')) {
        base64data = imageUri.split(',')[1];
      } else {
        // For file:// URIs, we need to read the file
        // Using a simple fetch approach that works in React Native
        const response = await fetch(imageUri);
        const blob = await response.blob();
        
        // Convert blob to base64
        return new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onloadend = async () => {
            try {
              base64data = reader.result.split(',')[1];
              await sendToAPI(base64data);
              resolve();
            } catch (error) {
              reject(error);
            }
          };
          reader.onerror = reject;
          reader.readAsDataURL(blob);
        });
      }
      
      await sendToAPI(base64data);
    } catch (error) {
      console.error('Error processing image:', error);
      Alert.alert(
        'Error',
        `Failed to process image: ${error.message}\n\nMake sure the API server is running and the API_URL is correct.`
      );
      setLoading(false);
    }
  };

  const sendToAPI = async (base64data) => {
    try {
      // Send to API
      const apiResponse = await fetch(`${API_URL}/detect`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: base64data,
          conf: 0.25,
        }),
      });

      if (!apiResponse.ok) {
        throw new Error(`API error: ${apiResponse.status}`);
      }

      const data = await apiResponse.json();
      
      if (data.error) {
        throw new Error(data.error);
      }

      setResult(data);
      setLoading(false);
    } catch (error) {
      console.error('Error sending to API:', error);
      Alert.alert(
        'Error',
        `Failed to process image: ${error.message}\n\nMake sure the API server is running and the API_URL is correct.`
      );
      setLoading(false);
      throw error;
    }
  };

  if (showCamera) {
    return (
      <CameraScreen onCapture={handleCameraCapture} onCancel={() => setShowCamera(false)} />
    );
  }

  return (
    <LinearGradient
      colors={['#667eea', '#764ba2', '#f093fb']}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
      style={styles.container}
    >
      <StatusBar style="light" />
      
      <View style={styles.header}>
        <Text style={styles.title} numberOfLines={1} adjustsFontSizeToFit={true}>🇹🇷 Halimi's Lira Counter</Text>
        <Text style={styles.subtitle}>Detect and count Turkish Lira bills</Text>
      </View>

      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.button} onPress={takePhoto} activeOpacity={0.8}>
          <LinearGradient
            colors={['#667eea', '#764ba2']}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
            style={styles.buttonGradient}
          >
            <Text style={styles.buttonText}>📷 Take Photo</Text>
          </LinearGradient>
        </TouchableOpacity>
        
        <TouchableOpacity style={styles.button} onPress={pickImage} activeOpacity={0.8}>
          <LinearGradient
            colors={['#f093fb', '#f5576c']}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
            style={styles.buttonGradient}
          >
            <Text style={styles.buttonText} numberOfLines={1} adjustsFontSizeToFit={true}>🖼️ Choose Gallery</Text>
          </LinearGradient>
        </TouchableOpacity>
      </View>

      {loading && (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#fff" />
          <Text style={styles.loadingText}>Processing image...</Text>
        </View>
      )}

      {image && !loading && (
        <ScrollView style={styles.scrollView}>
          <View style={styles.imageContainer}>
            <Image source={{ uri: image }} style={styles.image} />
          </View>
          
          {result && (
            <View style={styles.resultContainer}>
              <LinearGradient
                colors={['#11998e', '#38ef7d']}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 1 }}
                style={styles.totalContainer}
              >
                <Text style={styles.totalLabel}>Total Amount</Text>
                <Text style={styles.totalAmount}>{result.total_amount} Lira</Text>
                <Text style={styles.billsCount}>{result.total_bills} bill(s) detected</Text>
              </LinearGradient>

              {result.detections && result.detections.length > 0 && (
                <LinearGradient
                  colors={['rgba(255,255,255,0.95)', 'rgba(255,255,255,0.98)']}
                  style={styles.breakdownContainer}
                >
                  <Text style={styles.breakdownTitle}>Breakdown:</Text>
                  {Object.entries(result.counts)
                    .filter(([_, count]) => count > 0)
                    .sort(([a], [b]) => parseInt(a) - parseInt(b))
                    .map(([denomination, count]) => {
                      const value = parseInt(denomination);
                      const subtotal = value * count;
                      return (
                        <View key={denomination} style={styles.breakdownItem}>
                          <Text style={styles.denomination}>{denomination} Lira</Text>
                          <Text style={styles.count}>× {count}</Text>
                          <Text style={styles.subtotal}>= {subtotal} Lira</Text>
                        </View>
                      );
                    })}
                </LinearGradient>
              )}

              {result.annotated_image && (
                <LinearGradient
                  colors={['rgba(255,255,255,0.95)', 'rgba(255,255,255,0.98)']}
                  style={styles.annotatedContainer}
                >
                  <Text style={styles.annotatedTitle}>Annotated Image:</Text>
                  <Image
                    source={{ uri: `data:image/jpeg;base64,${result.annotated_image}` }}
                    style={styles.annotatedImage}
                  />
                </LinearGradient>
              )}
            </View>
          )}
        </ScrollView>
      )}

      {!image && !loading && (
        <View style={styles.placeholderContainer}>
          <Text style={styles.placeholderText}>
            Select an image to detect cash bills
          </Text>
        </View>
      )}
    </LinearGradient>
  );
}

function CameraScreen({ onCapture, onCancel }) {
  const [facing, setFacing] = useState('back');
  const cameraRef = React.useRef(null);

  const takePicture = async () => {
    if (cameraRef.current) {
      try {
        const photo = await cameraRef.current.takePictureAsync({
          quality: 0.8,
          base64: true, // Get base64 for easier processing
        });
        if (photo && photo.uri) {
          // If base64 is available, use it; otherwise use URI
          if (photo.base64) {
            onCapture(`data:image/jpeg;base64,${photo.base64}`);
          } else {
            onCapture(photo.uri);
          }
        }
      } catch (error) {
        console.error('Error taking picture:', error);
        Alert.alert('Error', 'Failed to take picture');
      }
    }
  };

  return (
    <View style={styles.cameraContainer}>
      <CameraView
        style={styles.camera}
        facing={facing}
        ref={cameraRef}
      >
        <View style={styles.cameraControls}>
          <TouchableOpacity style={styles.cancelButton} onPress={onCancel}>
            <Text style={styles.cancelButtonText}>Cancel</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.captureButton} onPress={takePicture}>
            <View style={styles.captureButtonInner} />
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.flipButton}
            onPress={() => setFacing(facing === 'back' ? 'front' : 'back')}
          >
            <Text style={styles.flipButtonText}>Flip</Text>
          </TouchableOpacity>
        </View>
      </CameraView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: Platform.OS === 'ios' ? 50 : 30,
  },
  header: {
    alignItems: 'center',
    paddingVertical: 28,
    paddingHorizontal: 20,
    backgroundColor: 'transparent',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 6,
    letterSpacing: 0.5,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 15,
    color: 'rgba(255,255,255,0.9)',
    fontWeight: '400',
    textShadowColor: 'rgba(0,0,0,0.2)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 2,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 24,
    gap: 12,
  },
  button: {
    flex: 1,
    borderRadius: 16,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.3,
    shadowRadius: 12,
    elevation: 8,
    minHeight: 56,
  },
  buttonGradient: {
    flex: 1,
    paddingVertical: 16,
    paddingHorizontal: 12,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 16,
  },
  buttonText: {
    color: '#fff',
    fontSize: 15,
    fontWeight: '700',
    textAlign: 'center',
    flexShrink: 1,
    textShadowColor: 'rgba(0,0,0,0.2)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 2,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 20,
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 3,
  },
  scrollView: {
    flex: 1,
  },
  imageContainer: {
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 16,
    paddingHorizontal: 12,
    backgroundColor: 'transparent',
  },
  image: {
    width: '100%',
    aspectRatio: 1.2,
    resizeMode: 'contain',
    backgroundColor: 'rgba(255,255,255,0.95)',
    borderRadius: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.2,
    shadowRadius: 16,
    elevation: 10,
  },
  resultContainer: {
    padding: 16,
  },
  totalContainer: {
    padding: 32,
    borderRadius: 24,
    alignItems: 'center',
    marginBottom: 20,
    shadowColor: '#11998e',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.4,
    shadowRadius: 16,
    elevation: 12,
  },
  totalLabel: {
    color: '#fff',
    fontSize: 17,
    marginBottom: 8,
    fontWeight: '500',
    letterSpacing: 0.5,
    textTransform: 'uppercase',
  },
  totalAmount: {
    color: '#fff',
    fontSize: 48,
    fontWeight: 'bold',
    letterSpacing: 1,
  },
  billsCount: {
    color: '#fff',
    fontSize: 15,
    marginTop: 8,
    opacity: 0.95,
    fontWeight: '400',
  },
  breakdownContainer: {
    borderRadius: 20,
    padding: 24,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
    elevation: 8,
  },
  breakdownTitle: {
    fontSize: 20,
    fontWeight: '700',
    marginBottom: 16,
    color: '#1a1a1a',
  },
  breakdownItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  denomination: {
    fontSize: 17,
    fontWeight: '600',
    color: '#1a1a1a',
    flex: 1,
  },
  count: {
    fontSize: 16,
    color: '#6c757d',
    marginRight: 16,
    fontWeight: '500',
  },
  subtotal: {
    fontSize: 17,
    fontWeight: '700',
    color: '#28a745',
  },
  annotatedContainer: {
    borderRadius: 20,
    padding: 24,
    marginTop: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
    elevation: 8,
  },
  annotatedTitle: {
    fontSize: 20,
    fontWeight: '700',
    marginBottom: 16,
    color: '#1a1a1a',
  },
  annotatedImage: {
    width: '100%',
    height: 300,
    resizeMode: 'contain',
    borderRadius: 12,
    backgroundColor: '#f8f9fa',
  },
  placeholderContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 40,
  },
  placeholderText: {
    fontSize: 20,
    color: 'rgba(255,255,255,0.8)',
    textAlign: 'center',
    lineHeight: 28,
    fontWeight: '500',
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 3,
  },
  cameraContainer: {
    flex: 1,
    backgroundColor: '#000',
  },
  camera: {
    flex: 1,
  },
  cameraControls: {
    flex: 1,
    backgroundColor: 'transparent',
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'flex-end',
    paddingBottom: 50,
    paddingHorizontal: 20,
  },
  cancelButton: {
    backgroundColor: 'rgba(0,0,0,0.7)',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 25,
    borderWidth: 2,
    borderColor: '#fff',
  },
  cancelButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  captureButton: {
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.4,
    shadowRadius: 8,
    elevation: 8,
  },
  captureButtonInner: {
    width: 68,
    height: 68,
    borderRadius: 34,
    backgroundColor: '#007bff',
  },
  flipButton: {
    backgroundColor: 'rgba(0,0,0,0.7)',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 25,
    borderWidth: 2,
    borderColor: '#fff',
  },
  flipButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

