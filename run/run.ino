int led = 13; // EEEEI ATENCAO AQUIIIII 0.0

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop(){
  char leitura = Serial.read();
  if(leitura == '1'){
    digitalWrite(led, HIGH);
  }
  else if(leitura == '0'){
    digitalWrite(led, LOW);
  }
}
