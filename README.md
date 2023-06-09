# Projekt-SI
Projekt zaliczeniowy 

Filip Bąk 148859

Opis rzeczywistego problemu.  (0 pkt)

Monitorowanie stanu balonu stratosferycznego w trakcie trwania lotu celem weryfikacji integralności powłoki nośnej, oraz jej rozmiarów a w przyszłości celem potwierdzenia poprawnego otwarcia spadochronu

State of art (3 pkt)

Proponowany problem nie ma jeszcze innych rozwiązań, a przynajmniej takich dostępnych dla wiadomości publicznej, jednakże proponowane rozwiązanie polega na wykrywaniu kształtu za pomocą transformaty Hougha, są jeszcze rozwiązania pozwalające na detekcję kształtu na bazie deskryptora cech, metody bazujące na segmentacji obrazu lub korzystające z sieci neuronowych.

Opis wybranej koncepcji (5 pkt)

Zdecydowałem się na wykrywanie kształtu w opencv. Wejściem programu jest obraz z kamery pokładowej, który następnie jest poddawany preprocesingowi aby podbić kontrast między balonem a niebem. Wyjściem algorytmu jest film z naniesioną informacją o wykryciu powłoki a także jej maksymalnym wykrytym rozmiarze podanym w pikselach. Zauważonym problemem jest spontaniczne wykrywanie zer z daty w lewym dolnym rogu nagrania jako balon z nieznanego mi powodu. Do realizacji w rzeczywistym świecie będzie potrzebny system pokładowy, składający się z kamery i mikrokontrolera.

Proof of concept (7 pkt)
Nagranie wyjściowe
https://youtu.be/d1MJpPDmS7U
