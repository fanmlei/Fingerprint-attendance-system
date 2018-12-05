#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include "FPMXX.h"
#include "DS3231.h"

uint8_t FPM_Address[] = { 0xFF, 0xFF, 0xFF, 0xFF };
uint8_t FPM_Password[] = { 0x00, 0x00, 0x00, 0x00 };

LiquidCrystal_I2C lcd(0x3F, 16, 2);
SoftwareSerial mySerial(3, 2);
FPMXX fs = FPMXX(&mySerial, FPM_Address, 9600);
RTClib RTC;

#define record 6
#define leave 9
#define confirm 10
#define cancel 11
#define buzzer 7
String cmd ;
uint16_t size = 0;
int finger_id, time_now, time_Refresh, id;

void setup() {
  Serial.begin(9600);
  pinMode(record, INPUT);
  pinMode(leave, INPUT);
  pinMode(confirm, INPUT);
  pinMode(cancel, INPUT);
  pinMode(buzzer, OUTPUT);
  lcd.init();                   //初始化lcd屏幕
  lcd.backlight();
  Wire.begin();
  sensor_init();
  showTime();
}

void loop() {
  Refresh();
  key();
  recive_data();
}


//初始化指纹识别模块
void sensor_init() {
  uint8_t r = fs.verifyPassword(FPM_Password);  //验证指纹模块
  switch (r)
  {
    case FPMXX_CODE_OK:
      lcd.print("OK");
      break;
    case FPMXX_REPLY_TIME_OUT:
      lcd.print("Connect failed");
      break;
  }
}


//获取指纹id
int get_finger_id() {
  uint8_t r;
  r = fs.getFingerImage();        //扫描指纹
  if (r == FPMXX_GET_IMAGE_NO_FINGER) {
    lcd.clear();
    lcd.print("Not Find Finger");   //手指没有放上去
    delay(200);
    if (digitalRead(cancel) == 1) {
      showTime();
      return -1;
    }
    get_finger_id();
  }

  else if (r == FPMXX_GET_IMAGE_FAILED) {
    lcd.clear();
    lcd.print("Scan Failed");       //扫描失败
    delay(200);
    get_finger_id();

  }
  else {
    fs.image2tz(1);                 //生成指纹特征
    uint16_t id = 0;                // 与指纹库进行匹配
    if (fs.searchFinger(1, 0, size - 1, &id) == FPMXX_CODE_OK) {
      return id;
    }
    else {
      delay(200);
      get_finger_id();
    }
  }
}

//更新指纹 id :指定id
void update_finger(int id) {
  //扫描指纹
  lcd.clear();
  lcd.print("Please scan finger...");
  while (fs.getFingerImage() != FPMXX_CODE_OK) {}
  lcd.clear();
  lcd.print("OK");
  //指纹图像生成特征
  fs.image2tz(1);
  delay(1000);
  //再扫描一遍
  lcd.clear();
  lcd.print("scan same finger again...");
  while (fs.getFingerImage() != FPMXX_CODE_OK) {}
  lcd.clear();
  lcd.print("OK");

  fs.image2tz(2);
  fs.buildTemplate();
  fs.storeFinger(1, id);
  lcd.clear();
  lcd.print("Add New Finger");
  lcd.setCursor(0, 1);
  lcd.print("ID:");
  lcd.print(id);
  digitalWrite(buzzer, HIGH);
  delay(200);
  digitalWrite(buzzer, LOW);
  delay(200);
  digitalWrite(buzzer, HIGH);
  delay(200);
  digitalWrite(buzzer, LOW);
  delay(200);
  showTime();
}

//新增指纹
void add_new_finger() {
  //获取当前已存指纹数目
  uint16_t num = 0;
  fs.getFingerNum(&num);
  lcd.clear();
  lcd.print("Please scan finger...");
  while (fs.getFingerImage() != FPMXX_CODE_OK) {}
  lcd.clear();
  lcd.print("OK");
  //指纹图像生成特征
  fs.image2tz(1);
  delay(1000);
  //再扫描一遍
  lcd.clear();
  lcd.print("scan same finger again...");
  while (fs.getFingerImage() != FPMXX_CODE_OK) {}
  lcd.clear();
  lcd.print("OK");
  fs.image2tz(2);
  fs.buildTemplate();
  fs.storeFinger(1, num + 1);
  lcd.clear();
  lcd.print("Add New Finger");
  lcd.setCursor(0, num + 1);
  lcd.print("ID:");
  lcd.print(num + 1);
  Serial.print("add:");
  Serial.print(num + 1 );
  digitalWrite(buzzer, HIGH);
  delay(200);
  digitalWrite(buzzer, LOW);
  delay(200);
  digitalWrite(buzzer, HIGH);
  delay(200);
  digitalWrite(buzzer, LOW);
  delay(200);
  showTime();
}

//接收上位机发送过来的指令
int recive_data() {
  while (Serial.available() > 0)
  {
    cmd += char(Serial.read());
    delay(2);
  }
  if (cmd.length() > 0 && cmd.length() < 5)
  {
    update_finger(cmd.toInt());
    cmd = "";
  }
  else if (cmd.length() > 5)
  {
    add_new_finger();
    cmd = "";
  }
}

void Refresh()                                  //刷新时钟显示
{
  time_now = millis();
  if (time_now - time_Refresh >= 30000)
  {
    time_Refresh = millis();
    showTime();
  }
}

void key() {
  if (digitalRead(record) == 1) {
    Record();
  }
  if (digitalRead(leave) == 1) {
    Leave();
  }
}

void Record() {
  finger_id = get_finger_id();
  if (finger_id > 0) {
    lcd.clear();
    lcd.print("Record Success");
    lcd.setCursor(0, 1);
    lcd.print("ID:");
    lcd.print(finger_id);
    Serial.print("record:");
    Serial.print(finger_id);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
    delay(200);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
    delay(200);
    showTime();
  }
}

void Leave() {
  finger_id = get_finger_id();
  if (finger_id > 0) {
    lcd.clear();
    lcd.print("Leave Success");
    lcd.setCursor(0, 1);
    lcd.print("ID:");
    lcd.print(finger_id);
    Serial.print("leave:");
    Serial.print(finger_id);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
    delay(200);
    digitalWrite(buzzer, HIGH);
    delay(200);
    digitalWrite(buzzer, LOW);
    delay(200);
    showTime();
  }
}


void showTime()
{
  lcd.clear();
  DateTime now = RTC.now();
  lcd.setCursor(0, 0);
  lcd.print(now.year(), DEC);
  lcd.print('/');
  lcd.print(now.month(), DEC);
  lcd.print('/');
  lcd.print(now.day(), DEC);
  lcd.print(' ');
  //lcd.setCursor(0, 1);
  lcd.print(now.hour(), DEC);
  lcd.print(':');
  lcd.print(now.minute(), DEC);
  //lcd.print(':');
  //  lcd.print(now.second(), DEC);
  //  lcd.print(' ');
  //  lcd.setCursor(9, 1);
}
