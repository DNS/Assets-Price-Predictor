
echo ------------- >> website-popularity.txt
date /t >> website-popularity.txt
echo; >> website-popularity.txt

python ..\Alexa-Rank\alexa.py matahari.com >> website-popularity.txt
python ..\Alexa-Rank\alexa.py zalora.co.id >> website-popularity.txt
python ..\Alexa-Rank\alexa.py berrybenka.com >> website-popularity.txt
python ..\Alexa-Rank\alexa.py tees.co.id >> website-popularity.txt
python ..\Alexa-Rank\alexa.py frozenshop.com >> website-popularity.txt

echo; >> website-popularity.txt
python ..\Alexa-Rank\alexa.py tokopedia.com >> website-popularity.txt
python ..\Alexa-Rank\alexa.py shopee.co.id >> website-popularity.txt
python ..\Alexa-Rank\alexa.py bukalapak.com >> website-popularity.txt
python ..\Alexa-Rank\alexa.py lazada.co.id >> website-popularity.txt
python ..\Alexa-Rank\alexa.py olx.co.id >> website-popularity.txt
python ..\Alexa-Rank\alexa.py jd.id >> website-popularity.txt

echo; >> website-popularity.txt
python ..\Alexa-Rank\alexa.py dns.xyz >> website-popularity.txt


pause
