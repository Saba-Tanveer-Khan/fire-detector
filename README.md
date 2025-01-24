# IoT-Based Fire Detection System

An IoT-based fire detection system that uses sensors to detect potential fire hazards in real time. The system provides alerts through a buzzer and sends notifications via a Flask server, allowing for immediate action during emergencies.

---

## **Features**
- **Real-Time Monitoring:** Continuously monitors environmental conditions using IoT sensors.
- **Alerts:**
  - Buzzer sounds for warnings or critical situations.
  - Notifications sent through a Flask server for centralized monitoring.
- **Customizable Thresholds:** Adjustable distance thresholds for hazard detection.
- **Scalability:** Can be extended to integrate with cloud platforms or additional sensors.

---

## **Technologies Used**
- **IoT Hardware:**
  - Ultrasonic sensors for measuring distance (e.g., smoke/obstacles).
  - Buzzer for audible alerts.
- **Programming Languages:**
  - Arduino (C++) for hardware control.
  - Python for server-side development.
- **Frameworks:** Flask for server-based real-time alert delivery.

---

## **Getting Started**
### **Hardware Requirements**
1. Microcontroller (e.g., Arduino Uno)
2. Ultrasonic sensor
3. Buzzer
4. Connecting wires and breadboard

### **Software Requirements**
1. Arduino IDE for programming the microcontroller.
2. Python 3.x for running the Flask server.
3. Flask framework for real-time communication.

---

## **Installation**
1. Set up the hardware as per the circuit design.
2. Upload the Arduino sketch to the microcontroller.
3. Install Flask in your Python environment using:
   ```bash
   pip install flask
