import tweepy
import re
import os
credential_path = r'/home/key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from datetime import datetime, timedelta
#from nltk.tokenize import WordPunctTokenizer

#keys to access twitter Api
ACC_TOKEN = ''
ACC_SECRET = ''
CONS_KEY = ''
CONS_SECRET = ''

#function to verify the api keys
def authentication(cons_key, cons_secret, acc_token, acc_secret):
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)
    return api
def search_tweets(keyword, total_tweets):

    api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)
    #search_result = tweepy.Cursor(api.search, q=keyword, since=yesterday_date, result_type='recent',lang='en').items(total_tweets)
    search_result = api.search(keyword, count=total_tweets)
    return search_result

def clean_tweets(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
   # lower_case_tweet= number_removed.lower()
    #tok = WordPunctTokenizer()
    #words = tok.tokenize(lower_case_tweet)
    #clean_tweet = (' '.join(words)).strip()
    clean_tweet = number_removed
    return clean_tweet

def get_sentiment_score(tweet):
    client = language.LanguageServiceClient()
    document = types\
               .Document(content=tweet,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score

def analyze_tweets(keyword, total_tweets,h):
    h=[]
    score = 0
    tweets = search_tweets(keyword,total_tweets)
    for tweet in tweets:
        cleaned_tweet = clean_tweets(tweet.text.encode('utf-8'))
        sentiment_score = get_sentiment_score(cleaned_tweet)
        score += sentiment_score
        print('Tweet: {}'.format(cleaned_tweet))
        print('Score: {}\n'.format(sentiment_score))
    final_score = round((score / float(total_tweets)),2)
    h.append(final_score)
    return final_score


if __name__ == '__main__':
    b=[]
    analyze_tweets('hate',50,b)


"""----------------------------------------------------------------op
************************************  OUTPUT    ********************************************
Tweet: I m done being nice i overplay my part everytime   Y all gone hate this new me
Score: -0.800000011921

Tweet:  Imo  c est excellent    H te de voir le rendu finale
Score: 0.899999976158

Tweet: RT  a      sharing her approval of Jeff s Twitter activities and how widely shared h
Score: 0.10000000149

Tweet: RT   Hate destroys  love builds  be a creator  Fear closes  love opens  be an advocate for life  Guilt stagnates  love pe
Score: -0.20000000298

Tweet: RT   i promise u idgaf how small it is  if I don t like something  I don t like it   amp  if u keep on doing it  you gon make me hate
Score: -0.899999976158

Tweet: RT   How yall complain about everything but the actual issues of DragonBall  I hate anime fans  These renders look fine if not grea
Score: -0.300000011921

Tweet: RT   Excited to try this  No mint hate allowed
Score: 0.300000011921

Tweet: Aghh yes  the hate can continue to escalate
Score: -0.5

Tweet:  Idk but I hate her
Score: -0.800000011921

Tweet:   Davila   Give an example if a comment that demonstrates clear hatred t
Score: -0.600000023842

Tweet: RT   I swear to god I hear another woman singing with Billie  You make me hate this city   Happier Than Ever remix  I hope n
Score: -0.800000011921

Tweet: I hate Internet Protestants
Score: -0.800000011921

Tweet: Hate the man I ve turned into
Score: -0.800000011921

Tweet: RT   Nah be proud  Heritage not hate right
Score: 0.0

Tweet:      I feel like people who feel like outcasts clung onto horror  And now that someone widely popular is embra
Score: -0.800000011921

Tweet: RT    But I say unto you which hear  Love your enemies  do good to them which hate you   Bless them that curse you  and pray f
Score: -0.800000011921

Tweet: i hate their priest so much
Score: -0.800000011921

Tweet: RT   ppl really pull shit out of their ass to hate on svt as if they aren t one of the most popular groups in the industry
Score: -0.899999976158

Tweet: It s really hard for me to do this but I hate dwelling on past and reliving traumatic moments so I will sweep shit
Score: -0.600000023842

Tweet: RT   Readout of Justice Department  HHS Listening Session on the Bipartisan COVID    Hate Crimes Act with Organizations Repr
Score: 0.0

Tweet:  I am so sorry  I hate hearing that your going through a lot
Score: -0.800000011921

Tweet: RT    i love soc but i hate kaz
Score: -0.5

Tweet: i hate  so much  fix your shit i stg
Score: -0.800000011921

Tweet: RT   Do you still hate yourself today
Score: -0.899999976158

Tweet: U don t hate me right  lol
Score: 0.40000000596

Tweet: i don t trust anyone rn and i hate it
Score: -0.800000011921

Tweet: RT   Nah be proud  Heritage not hate right
Score: 0.0

Tweet:  i hate it here
Score: -0.899999976158

Tweet: In a moment of anger tonight I may tweet  I fucking hate baseball   This is normal behavior for me in October  please don t read into it
Score: -0.899999976158

Tweet: RT   Nah be proud  Heritage not hate right
Score: 0.0

Tweet: RT   Imag nate haberle tirado hate a Luis Enrique toda la semana y hoy tenerte que ir a dormir calentito calentito
Score: -0.300000011921

Tweet: I feel like the bar hasn t even moved in the last   minutes    I ABSOLUTELY HATE THIS
Score: -0.800000011921

Tweet: RT      i hate uk weather why do i have to contemplate wearing my coat every morning
Score: -0.10000000149

Tweet: RT   I hate being a taurus why can t I get over stuff in like   minutes  I don t want to hold lifelong grudges
Score: -0.899999976158

Tweet: I hate Hufflepuffs  They always go to Azkaban  no matter what I say
Score: -0.800000011921

Tweet:  I hate that I m a part of the other
Score: -0.800000011921

Tweet: RT   I hate the whole   if they wanted to  they would  bc sometimes I want to and I don t
Score: -0.800000011921

Tweet: RT   So in a bid to discredit IPOB the governm nt actually used DSS as unknown gunm n to stir up probl ms and turn around to blam
Score: -0.699999988079

Tweet: RT   hate how fast my mood changes over the smallest things
Score: -0.699999988079

Tweet: RT   i need some love to go with this hate
Score: -0.600000023842

Tweet: RT   i promise u idgaf how small it is  if I don t like something  I don t like it   amp  if u keep on doing it  you gon make me hate
Score: -0.899999976158

Tweet: Bro we re going on an hour now of       and I couldn t hate Ticketmaster more
Score: -0.699999988079

Tweet: RT   Y all claim to hate Wizkid s Made in Lagos but the numbers saying you stream the music  The math not mathing
Score: -0.699999988079

Tweet:  Yo Kai can you help me out  Dan unfortunately blocked me idk why but I m actually a decent fan of hi
Score: -0.10000000149

Tweet: RT   How Is This Appalling  Racist Harassment in Virginia Beach NOT Considered a Hate Crime   It s certainly  intended to inti
Score: -0.699999988079

Tweet: RT   Trop h te
Score: -0.40000000596

Tweet:  bandicoot      Same  And that    platinum awards trophy  Man  I just hate online trophies I suck at it so bad LMFAO
Score: -0.800000011921

Tweet: RT   I hate when girls die
Score: -0.800000011921

Tweet: RT  bamba  I HATE when people lose shit around me  Hurry up and find it cause WTF you trying say
Score: -0.899999976158

Tweet: RT   I hate everyone for not telling me this exists    JIN  SEOKJIN  BTSJIN
Score: -0.800000011921"""
