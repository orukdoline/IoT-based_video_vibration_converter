#include <WiFiS3.h>

#include "arduino_secrets.h" 
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

int status = WL_IDLE_STATUS;
WiFiServer server(23);

const int vibrationPin = 3;
boolean alreadyConnected = false;

// WiFi 연결 및 서버 시작, 진동 모터 핀 설정
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }

  server.begin();
  printWifiStatus();
  
  pinMode(vibrationPin, OUTPUT);
}

// 클라이언트 연결 및 입력값에 따라 진동 모터 제어
void loop() {
  WiFiClient client = server.available();

  if (client) {
    if (!alreadyConnected) {
      client.flush();
      Serial.println("We have a new client");
      client.println("Hello, client!");
      alreadyConnected = true;
    }

    if (client.available() > 0) {
      String clientInput = client.readStringUntil('\n');
      int value = clientInput.toInt(); // convert the received string to an integer

      if (value >= 1 && value <= 5) {
        int outputValue = map(value, 1, 5, 0, 255);
        analogWrite(vibrationPin, outputValue);
      }

      Serial.println(clientInput);
    }
  }
}

// WiFi 연결 상태 및 IP 주소, 신호 강도 출력
void printWifiStatus() {
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
