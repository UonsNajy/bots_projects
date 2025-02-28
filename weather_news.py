#استيراد مكتبه request للتعامل معا api
import requests
#تعيين URL الخاص ب الاخبار باستخدام api
NEWS_API_KEY = "f9271264fa3d45e0a9d2b3a0e0fb93ab"
NEW_URL = f'https//newsapi.org/v2/top-headlines?country=ye&apiKey={NEWS_API_KEY}'

#كتابه داله لجلب الاخبار من News api
def get_news():
    #ارسال طلب الى  api للحصول على الاخبار
    response = requests.get(NEW_URL)
    #تحويل الاستجابه الى جيسون
    data = response.json()
    #استخراج المقالات من الاستجابه
    articles = data.get("articles",[])
    #استخلراج العناوين ودمجها في نص واحد
    news_list = [f"-{article['title']}" for article in articles[:5]]
    return "\n".join(news_list)
#اختبار داله الاخبار 
print(get_news())

#تعيين URL الخاص بالطقس ب استخدام OpenWEathermap  و مفتاحapi
weather_API_KEY = "43309e666e64961c5be73cf363f58924"
#المدينه التي ترغب في معرفه الطقس فيها 
CITY = "amran"
weather_URL = f"http//api.openweathermap.org/data2.5/weather?q={CITY}&appid={weather_API_KEY}&units=metric"

#كتابه داله لجلب الطقس من openweathermap
def get_weather():
    response = requests.get(weather_URL)
    data = response.json()
    #استخراج درجه الحراره 
    temp = data['main']['temp']
    #استخراج وصف الطقس
    description = data['weather'][0]['description']
    return f'الطقس في -C{temp}: {CITY} {description}'

print(get_weather())