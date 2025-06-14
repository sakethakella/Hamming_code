# 🔮 Jujutsu Kaisen: Geto's Curse Decoder

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/OpenCV-4.0+-green.svg" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/NumPy-Latest-orange.svg" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Status-Complete-success.svg" alt="Status"/>
</div>

<div align="center">
  <h3>🚨 <em>Spoiler Alert!</em> 🚨</h3>
  <p><strong>Unveiling the Hidden Plan: Overcoming Geto's Curse</strong></p>
</div>

---

## 📖 **Story Overview**

<p>Embark on a daring mission to assist <strong>Mechamaru</strong> in encoding crucial information about <strong>Geto's plan</strong>. Meanwhile, <strong>Yuji</strong> and <strong>Megumi</strong> must decode the image ensnared by Geto, Jogo, and Mahito holding Gojo in the Prison Realm. Despite the disruptive <strong>Gigantic Veil (Tobari)</strong> cast by Geto, your mission is to decode the image and thwart Geto's scheme!</p>

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>🤖 Mechamaru</strong><br/><em>Encoder</em></td>
      <td align="center"><strong>🌪️ Geto's Veil</strong><br/><em>Channel Noise</em></td>
      <td align="center"><strong>⚡ Yuji & Megumi</strong><br/><em>Decoder Team</em></td>
    </tr>
  </table>
</div>

---

## 🎯 **Objective**

<p>This project implements a <strong>Hamming Error Correction Code</strong> system disguised as a Jujutsu Kaisen mission:</p>

<ol>
  <li><strong>Encode</strong> an image using Hamming(8,4) error correction</li>
  <li><strong>Simulate</strong> channel errors (Geto's curse) with random bit flips</li>
  <li><strong>Decode</strong> and correct errors to recover the original image</li>
  <li><strong>Apply XOR decryption</strong> to reveal the final hidden message</li>
</ol>

---

## 🛠️ **Technical Implementation**

### **Algorithm: Hamming(8,4) Code**

<div align="center">
  <table border="1">
    <tr>
      <th>Bit Position</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Purpose</th>
      <td>P1</td>
      <td>P2</td>
      <td>P3</td>
      <td>D1</td>
      <td>P4</td>
      <td>D2</td>
      <td>D3</td>
      <td>D4</td>
    </tr>
  </table>
</div>

<ul>
  <li><strong>P1, P2, P3, P4</strong>: Parity bits for error detection/correction</li>
  <li><strong>D1, D2, D3, D4</strong>: Data bits (4 bits of actual image data)</li>
</ul>

### **Error Correction Formula**

<pre>
<code>
c1 = D1 ⊕ D2 ⊕ D4
c2 = D1 ⊕ D3 ⊕ D4  
c3 = D2 ⊕ D3 ⊕ D4
c4 = D2 ⊕ D3 ⊕ D4

Error Position = 4×c3 + 2×c2 + 1×c1
</code>
</pre>

---

## 📁 **Project Structure**

<pre>
<code>
jujutsu-kaisen-decoder/
├── 📄 binary_con.py           # Mechamaru's Encoder
├── 📄 Channel.py              # Geto's Veil (Error Simulation)  
├── 📄 decoding.py             # Yuji & Megumi's Decoder
├── 📄 README.md               # This file
├── 🖼️ image.png               # Original input image
├── 🗃️ output.bin              # Encoded data
├── 🗃️ received.bin            # Data after channel errors
├── 🗃️ Array_to_be_Xored.bin   # Geto's curse (XOR mask)
└── 🖼️ outputimage.png         # Final decoded image
</code>
</pre>

---

## 🚀 **Installation & Setup**

### **Prerequisites**

<pre>
<code>
pip install opencv-python numpy
</code>
</pre>

### **Required Files**

<ul>
  <li><code>image.png</code> - Original grayscale image (will be resized to 1000×500)</li>
  <li><code>Array_to_be_Xored.bin</code> - XOR mask for final decryption</li>
</ul>

---

## ▶️ **Usage Instructions**

### **Step 1: Encode the Image (Mechamaru's Mission)**

<pre>
<code>
python binary_con.py
</code>
</pre>

<details>
<summary><strong>What this does:</strong></summary>
<ul>
  <li>Loads <code>image.png</code> and converts to grayscale</li>
  <li>Resizes to <strong>1000×500</strong> pixels (500,000 pixels total)</li>
  <li>Flattens to binary stream (4,000,000 bits)</li>
  <li>Applies <strong>Hamming(8,4)</strong> encoding</li>
  <li>Saves encoded data to <code>output.bin</code></li>
</ul>
</details>

### **Step 2: Simulate Channel Errors (Geto's Veil)**

<pre>
<code>
python Channel.py
</code>
</pre>

<details>
<summary><strong>What this does:</strong></summary>
<ul>
  <li>Introduces random bit flips with <strong>2% error probability</strong></li>
  <li>Simulates real-world communication channel noise</li>
  <li>Saves corrupted data to <code>received.bin</code></li>
</ul>
</details>

### **Step 3: Decode & Recover (Yuji & Megumi's Teamwork)**

<pre>
<code>
python decoding.py
</code>
</pre>

<details>
<summary><strong>What this does:</strong></summary>
<ul>
  <li>Reads corrupted data from <code>received.bin</code></li>
  <li>Applies <strong>Hamming error correction</strong> to each 8-bit codeword</li>
  <li>Recovers original 4-bit data segments</li>
  <li>XORs with <code>Array_to_be_Xored.bin</code> to break Geto's final curse</li>
  <li>Displays and saves the recovered image as <code>outputimage.png</code></li>
</ul>
</details>

---

## 🔧 **Code Breakdown**

### **Encoding Process (`binary_con.py`)**

<pre>
<code>
def hamming(input, output):
    # Place data bits
    output[7] = input[3]  # D4
    output[6] = input[2]  # D3  
    output[5] = input[1]  # D2
    output[3] = input[0]  # D1
    
    # Calculate parity bits
    output[0] = input[0] ^ input[1] ^ input[2] ^ input[3]  # P1
    output[1] = input[0] ^ input[1] ^ input[3]             # P2
    output[2] = input[0] ^ input[2] ^ input[3]             # P3
    output[4] = input[2] ^ input[1] ^ input[3]             # P4
</code>
</pre>

### **Decoding Process (`decoding.py`)**

<pre>
<code>
def hamming_decode(input, output):
    # Check parity bits
    c1 = input[1] ^ input[3] ^ input[5] ^ input[7]
    c2 = input[2] ^ input[3] ^ input[5] ^ input[7]  
    c3 = input[4] ^ input[5] ^ input[6] ^ input[7]
    c4 = input[3] ^ input[5] ^ input[6] ^ input[7]
    
    # Calculate error position
    num = (4*c3) + (2*c2) + (1*c1)
    
    # Correct error if detected
    if num != 0:
        input[num] = input[num] ^ 1
    
    # Extract corrected data
    output[0] = input[3]  # D1
    output[1] = input[5]  # D2
    output[2] = input[6]  # D3
    output[3] = input[7]  # D4
</code>
</pre>

---

## 📊 **Performance Metrics**

<div align="center">
  <table>
    <tr>
      <th>Metric</th>
      <th>Value</th>
    </tr>
    <tr>
      <td><strong>Error Correction Capability</strong></td>
      <td>1-bit per 8-bit codeword</td>
    </tr>
    <tr>
      <td><strong>Code Rate</strong></td>
      <td>4/8 = 50%</td>
    </tr>
    <tr>
      <td><strong>Channel Error Rate</strong></td>
      <td>2% (configurable)</td>
    </tr>
    <tr>
      <td><strong>Image Dimensions</strong></td>
      <td>1000 × 500 pixels</td>
    </tr>
  </table>
</div>

---

## 🧪 **Testing & Validation**

<p>The system's effectiveness can be measured by:</p>

<ol>
  <li><strong>Visual comparison</strong> between original and decoded images</li>
  <li><strong>Peak Signal-to-Noise Ratio (PSNR)</strong> calculations</li>
  <li><strong>Bit Error Rate (BER)</strong> before and after correction</li>
  <li><strong>Structural Similarity Index (SSIM)</strong> for image quality assessment</li>
</ol>

---

## 🐛 **Troubleshooting**

<details>
<summary><strong>Common Issues</strong></summary>

<p><strong>Image not displaying properly?</strong></p>
<ul>
  <li>Ensure OpenCV is properly installed</li>
  <li>Check that image dimensions are exactly 1000×500 after processing</li>
</ul>

<p><strong>File not found errors?</strong></p>
<ul>
  <li>Make sure all required <code>.bin</code> files are in the project directory</li>
  <li>Run scripts in the correct order: encoder → channel → decoder</li>
</ul>

<p><strong>Memory issues?</strong></p>
<ul>
  <li>The project processes 4M bits of data - ensure sufficient RAM</li>
  <li>Consider processing in smaller chunks for very large images</li>
</ul>

</details>

---

## 🎨 **Customization Options**

### **Adjust Error Rate**

<pre>
<code>
# In Channel.py
error_probability = 0.05  # Change from 0.02 to 5% error rate
</code>
</pre>

### **Change Image Dimensions**

<pre>
<code>
# In binary_con.py  
resized_image = cv2.resize(image, (width, height))  # Modify as needed
</code>
</pre>

### **Different Error Correction Codes**

<p>The framework can be extended to support:</p>
<ul>
  <li><strong>BCH Codes</strong></li>
  <li><strong>Reed-Solomon Codes</strong></li>
  <li><strong>Turbo Codes</strong></li>
  <li><strong>LDPC Codes</strong></li>
</ul>

---

## 📜 **License**

<p>This project is released under the <strong>MIT License</strong>. Feel free to use, modify, and distribute as needed.</p>

---

## 🙏 **Acknowledgments**

<ul>
  <li><strong>Gege Akutami</strong> - Creator of Jujutsu Kaisen manga</li>
  <li><strong>Richard Hamming</strong> - Inventor of Hamming codes</li>
  <li><strong>OpenCV Community</strong> - Image processing library</li>
  <li><strong>NumPy Developers</strong> - Numerical computing foundation</li>
</ul>

---

<div align="center">
  <h3>⚡ <em>"The strongest sorcerer in history vs. the strongest error correction code of today!"</em> ⚡</h3>
  
  <p><strong>Mission Status: ✅ COMPLETE</strong></p>
  <p><em>Geto's curse has been broken, and Gojo's image has been successfully recovered!</em></p>
</div>

---

<div align="center">
  <sub>Built with ❤️ for the Jujutsu Kaisen and coding communities</sub>
</div>
