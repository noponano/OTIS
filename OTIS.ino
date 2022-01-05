#include <SPI.h>
#include <NRFLite.h>

const static uint8_t RADIO_ID = 1;
const static uint8_t DESTINATION_RADIO_ID = 0;
const static uint8_t PIN_RADIO_CE = 9;
const static uint8_t PIN_RADIO_CSN = 10;

struct RadioPacket
{
  uint8_t RadioId;
  char Message[31];    // Note the max packet size is 32, so 31 is all we can use here.
};
NRFLite _radio;
RadioPacket packet;
//
//SoftwareSerial Serial2(2, 3);
String userinput = " ";
String userdata = "";
String str = "";

bool radioflag = true;
char inputdata[31];
#include <SoftwareSerial.h>
SoftwareSerial Serial2(2, 3);//blue and yellow
bool flag = true;
void setup() {
  // put your setup code here, to run once:
  if (!_radio.init(RADIO_ID, PIN_RADIO_CE, PIN_RADIO_CSN))
  {
    Serial.println("Cannot communicate with radio");
    while (1); // Wait here forever.
  }
  packet.RadioId = RADIO_ID;

  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {

  if (Serial2.available()) {
    char temp = char(Serial2.read());
    if (temp == '|')
      flag = true;
    else
      userdata += String(temp);
  }
  if (flag == true) {
    delay(30);
    {
      flag = false;
      int index = userdata.indexOf('T');
      String userinput = userdata.substring(index);
      str = userinput;
      radioflag = true;
    }
  }
  if (radioflag == true) {
    str.toCharArray(packet.Message, str.length() + 1);
    _radio.send(DESTINATION_RADIO_ID, &packet, sizeof(packet));
    Serial.println(str);


    radioflag = false;
    userdata = "";
    userinput = "";
  }
}
