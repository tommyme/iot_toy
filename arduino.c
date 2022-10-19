#include <SoftwareSerial.h>
SoftwareSerial monitor(8, 9); // RX, TX
int serial_putc( char c, struct __file * )
{
  Serial.write( c );
  monitor.write( c );
  return c;
}
void printf_begin(void)
{
  fdevopen( &serial_putc, 0 );
}
void setup(){
  Serial.begin(115200);
  monitor.begin(115200);
  printf_begin();
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
}
void loop(){
  int tv = analogRead(A5);
  int lv = analogRead(A4);
  printf("%d %d\n",tv,lv);
  if (lv > 700 || tv > 700)
  {
    digitalWrite(12, HIGH);
  }
  else
  {
    digitalWrite(12, LOW); 
  }
  delay(1000);
}