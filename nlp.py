import tweepy
import re
import os
credential_path = r'/home//key.json'
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
    search_result = api.search(keyword, count=total_tweets)
    return search_result

def clean_tweets(tweet):
    '''user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= number_removed.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()'''
    clean_tweet = tweet
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
    analyze_tweets('hello',50,b)












"""#####################################  OUTPUT #####################


Tweet: RT @Twitter: hello literally everyone
Score: 0.40000000596

Tweet: RT @nowthisnews: This diver caught an adorable moment on video when a wild grey seal swam up and hugged him underwater. Ben Burville says h…
Score: 0.20000000298

Tweet: RT @atlix2: “Hello, listeners.”
💟
(welcome to night vale au)
[rts &amp; comments appreciated]
#ranboofanart https://t.co/i9IVzYVMaj
Score: 0.40000000596

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: RT @kevinmw1999: Hello everyone, your favorite sibling duo are running for homecoming!! Voting ends Friday at 5, so be sure to vote #willia…
Score: 0.40000000596

Tweet: @dina10385101 @dina10385101   hello sorry to bother you I wonder if you can check out our youtube channel and tell… https://t.co/f0TV7KZw2S
Score: -0.20000000298

Tweet: hello sir the sad songs aren’t sad enough anymore
Score: -0.600000023842

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: Hello juniordanyw
Score: 0.300000011921

Tweet: @wasteddaysx @KennyHoopla Hello
Score: 0.300000011921

Tweet: @_arianie Girl HELLO, you’re in MY mentions, are you slow or are you dumb? As long as you mention me, I’m going to… https://t.co/j2J2y6p9cv
Score: -0.10000000149

Tweet: kak juniordanyw say hello donk for me
Score: 0.20000000298

Tweet: @sugalypse Hello, how are you?
On behalf of ahgases, I'm contacting you, @SublimeArtist_ , to talk about… https://t.co/SSlsQNmYMs
Score: 0.0

Tweet: RT @ActivismGhana: Hello Evans Mensah @Nuetey

Since you asked Mr Akoto Ampaw about which part of the anti-LGBTQ bill will criminalize "sym…
Score: -0.20000000298

Tweet: RT @honaghaahnii: hello. if any settlers have any wealth to redistribute, I’ve been hoping to get 2 air purifiers to help w allergies &amp; poo…
Score: -0.10000000149

Tweet: hello gordon
Score: 0.20000000298

Tweet: RT @kingsjaehwan: when jjaen first met sewoon, he asked for a selfie and introduced himself "hello i'm kim jaehwan! i've been watching you…
Score: 0.0

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @sethmpk @GovKathyHochul Hello all,JESUS and GOD love you all,which is why we can feel peace and happiness still.Yo… https://t.co/BA3PfYH1yQ
Score: 0.899999976158

Tweet: hello! early and long update today HAHA surprise,,, charot 😭 anyway next ud is bukas! https://t.co/j7PcpwIOEn
Score: 0.40000000596

Tweet: RT @_kimoprah: Hello from the other side 👋🏽 https://t.co/thulqCNBuy
Score: 0.0

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @bbxiao1 hello goodnight
Score: 0.20000000298

Tweet: RT @BusinessPunkNFT: Say goodbye to Wall Street &amp; HELLO to Virtual Street 👋

Website👉https://t.co/2cU5VuFjy2
OpenSea👉https://t.co/pjkzPvF2L…
Score: 0.10000000149

Tweet: RT @thatboyjww: hello carats paalala lang 😌 dahil ang daming artists ang magcomeback this october.

@pledis_17 #SEVENTEEN
#세븐틴 #Attacca ht…
Score: 0.0

Tweet: @adopt_a_roach hello i want a roach too pls
Score: -0.600000023842

Tweet: RT @RedoubtAFA: Hello all and happy Wednesday to anyone whose not a nazi. We are excited to finally introduce two Bitterroot Valley MT nazi…
Score: 0.699999988079

Tweet: RT @NobodyButNori_: Absolutely! “Hello Disney, yes I’m being harassed!”
Score: -0.20000000298

Tweet: RT @atlix2: “Hello, listeners.”
💟
(welcome to night vale au)
[rts &amp; comments appreciated]
#ranboofanart https://t.co/i9IVzYVMaj
Score: 0.40000000596

Tweet: @PoisonJL Hello sir!
Score: 0.600000023842

Tweet: RT @bchmpsgf: bs do br vcs estão a perder mimos acordem
Score: -0.20000000298

Tweet: @tubersnow HELLO IM FKIN OBSESSED ALREADH
Score: 0.40000000596

Tweet: hello there!, son las: 19:38:59
Score: 0.20000000298

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: Hello! sorry for the short break, my house was flooded by leaks so I couldn't draw ;v;;9
But I'm already catching u… https://t.co/wGBHgLMKdP
Score: 0.0

Tweet: @RealNaughtyMilf Hello
Score: 0.300000011921

Tweet: Hello RandyMartin98 ,,, say "RESMI" nya ditunggu loohh :3
Score: 0.899999976158

Tweet: hello friends https://t.co/resrYQOUt9
Score: 0.20000000298

Tweet: RT @MekaVerse: Hello everyone ! 🦾🤖
We're only 6 hours away from launching MekaVerse and the Raffle ⏰

↓ Here's our animated explanation vi…
Score: 0.10000000149

Tweet: RT @NOEA8Y: Red Lights hit 1M in 4 hours but Scars ??? hello ??? https://t.co/8yR077WgFH
Score: 0.0

Tweet: @sqvidley hello
Score: 0.20000000298

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: RT @T0riBird_: @splepytwt congrats splepy!! &lt;33
hello i draw fanart and sometimes my ocs! https://t.co/Vgk4NTS4kK
Score: 0.300000011921

Tweet: RT @ChibiLabs: @flurnft Hello, is it me you’re looking for? https://t.co/3RS7DkD9ou
Score: 0.10000000149

Tweet: @Jhoe_markk Hello, nice to meet you!
Score: 0.899999976158

Tweet: @denunciag7 hello, how are you?
on behalf of ahgases, i'm contacting you, @SublimeArtist_ , to talk about… https://t.co/i63XG6CbY6
Score: -0.10000000149

Tweet: RT @mylove4mu5ic: Say hello to 540’s newest sip and paint instructor ✨🤎 I’m SO excited to start this journey!!! https://t.co/ZraFMKkRXQ
Score: 0.600000023842

Tweet: RT @speckofyana: can we get a hello kitty emoji
Score: 0.0

Tweet: @malumsluvrr hello hello
Score: 0.20000000298

Tweet: Hello Autumn! 🌿🍂🌞
Close up painting from @BigTrunkTrail, @wildinart, @love_luton 🐘 #bigtrunktrail https://t.co/PByByuz3uN
Score: 0.300000011921

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @Diana_Cif24 Hello kitty 👀
Score: 0.300000011921

Tweet: RT @kcw18_: &amp; if y’all don’t like the lineup.. it’s more room for the ppl who do. HELLO MELLO!!!🥴🥴🥴
Score: 0.20000000298

Tweet: @hateoneanotter hello it’s me chris pratt i hate gay people and love god
Score: -0.40000000596

Tweet: @fcktns Hello, how are you?
On behalf of ahgases, I'm contacting you, @SublimeArtist_ , to talk about… https://t.co/2SnZ0lbNGT
Score: 0.0

Tweet: ✡✡

早く会いたい気持ちで　

早く連れて出て

NU'EST - HELLO
Score: 0.20000000298

Tweet: RT @kpcheer6: 今日は紫耀しか勝たんの紫耀くん♡
（私も苦手だけど1回言ってみたw）

ZIP!🐼✖️ King &amp; Prince 👑
『 恋降る月夜に君想ふ 』
 #KPの恋降るベラベラENGLISH
 #平野紫耀
Score: 0.10000000149

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: RT @LeftFlankVets: Hello hackers who released the Twitch payouts can you please delete the leaks we are being made fun of for not being ric…
Score: -0.699999988079

Tweet: @huntercyare MAVVVVVV HELLO
Score: 0.300000011921

Tweet: @HollyReslink Hello! How are you?
Score: 0.300000011921

Tweet: RT @thesoffgengar: ✨oh hello good eve once again it's generic bkdk hades and persephone au ft. more of cerberus uwu✨ https://t.co/aaHGHqlDn6
Score: 0.10000000149

Tweet: RT @dorksofprey: BLACK WIDOW DELETED SCENES HELLO??? https://t.co/oFtsfXmkdq
Score: 0.20000000298

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: RT @TWICESPACE_: Hello! Hoping you are having a great day! @997now Could you play #TheFeels by TWICE in your station please? 💖
Score: 0.40000000596

Tweet: RT @minersbIog: hello person i consider some thing under the lines of best friend. I am here to deliver a new character that people call an…
Score: 0.0

Tweet: RT @tinyheeje: retweet to spread.

hello engenes! because soon one of our favorite boys will have a birthday, yes heeseung! so i made this…
Score: 0.300000011921

Tweet: Another successful training under my belt… mom and I did so good that we get to say good bye to Lowes and hello to… https://t.co/x7iFx0GZoR
Score: 0.899999976158

Tweet: I always get a nice lil “hello sir” whenever I order food lmao
Score: 0.800000011921

Tweet: Hello, I'm Hajime Hinata. And as you can see, I'm gay
Score: 0.0

Tweet: RT @velv_0: Hello everyone! A bit of a odd post today but I want to know how many people would be listening to my nans story. I want to mak…
Score: 0.300000011921

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @Simon86276065 Hello sorry for the inconvenience, kindly send a direct message for assistance
Score: -0.20000000298

Tweet: RT @wattpad: Say hello to this month’s Community Curator, @Darlis_Steff! In celebration of Hispanic &amp; Latinx Heritage Month, she’s put toge…
Score: 0.20000000298

Tweet: RT @heychey: Hello…hi. Listen…

Vulnerability, marginalization.

These are NOT inherencies.

No one is coded as vulnerable.
No one is co…
Score: -0.10000000149

Tweet: RT @siteptbr: Hello, Emma! 5 anos atrás, a série derivada de "Scream" chegava ao fim na Netflix/MTV.

Com 2 temporadas impecáveis, elenco m…
Score: 0.40000000596

Tweet: hello
Score: 0.20000000298

Tweet: RT @BusinessPunkNFT: Say goodbye to Wall Street &amp; HELLO to Virtual Street 👋

Website👉https://t.co/2cU5VuFjy2
OpenSea👉https://t.co/pjkzPvF2L…
Score: 0.10000000149

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: hello https://t.co/1GXT810Qw1
Score: 0.20000000298

Tweet: RT @momosaku_www: Duet ソロ表紙🧡 本日発売
-------------------------
Snow Man 1st ALBUM
　 Snow Mania S1
2021.09.29 RELEASE
-------------------------…
Score: 0.10000000149

Tweet: @cincykid75 Hello dear friend!😃🤗😘🌹
Score: 0.800000011921

Tweet: @denunciag7 Hello, how are you?
On behalf of ahgases, I'm contacting you, @SublimeArtist_ , to talk about… https://t.co/Mq6t755Y0G
Score: 0.0

Tweet: RT @BusinessPunkNFT: Say goodbye to Wall Street &amp; HELLO to Virtual Street 👋

Website👉https://t.co/2cU5VuFjy2
OpenSea👉https://t.co/pjkzPvF2L…
Score: 0.10000000149

Tweet: @mxmclain @Anelajacklyn hello dear, feel free to hmu , email us at assignments864@gmail.com or whatsapp me on +1607… https://t.co/n45JKX9fFE
Score: 0.0

Tweet: @ianbremmer Hello all,JESUS and GOD love you all,which is why we can feel peace and happiness still.Youcan go to th… https://t.co/S9xB0M9aVt
Score: 0.899999976158

Tweet: RT @_byloey: [HELP RT]

Hello phixos and other fandoms! I am accepting academic commissions to assist students who are struggling due to b…
Score: 0.10000000149

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @yeaitsdamian @rozenlune Hello, dm me the homework details
Score: -0.20000000298

Tweet: @httpsabby_ hello** why is autocorrect beingweirf today
Score: -0.5

Tweet: 読んで後悔した
Score: -0.800000011921

Tweet: @olibluess Hello there. I would like to help you out with your assignments. I can provide high-quality, plagiarism-… https://t.co/ykFEDN6ukN
Score: 0.5

Tweet: @freer0bux2213 hello
Score: 0.20000000298

Tweet: @JlNLIP Hello
Score: 0.300000011921

Tweet: RT @jhanjhanfabila: "Hello"Tendered with understand. He tries to force the bad experiences in your god knows no
"No imagination. meaning .…
Score: -0.20000000298

Tweet: @Alg0nquin HELLO
Score: 0.300000011921

Tweet: @vventisbow @ultcatboy omg hello mun you're so cool
Score: 0.899999976158

mcaleb@cloudshell:~ (python-upload-312921)$


################################################################hate
weet: RT @leelpha: you gotta be sick in the head to hate him https://t.co/ndxVxN11zp
Score: -0.899999976158

Tweet: RT @Vegeta_Pchan: https://t.co/lSWHd4DiTP
Score: 0.0

Tweet: RT @fred_guttenberg: Texts from a student to a mother from today's school shooting.  Mother asks "Are you safe?"  Student relies "I don't k…
Score: -0.20000000298

Tweet: なんでじゃない！そなこと言

ツك͓̽و͓̽ب͓̽و͓̽ن͓̽ـُ

كـٍـٍـؤٍـٍـﺩ̲ خـّـصْــﻣ̝ ٌ̚

のنمشــــى　˜˜kc20˜˜

We don’t hate what w
3C078106
Score: 0.0

Tweet: RT @bbytorch: I hate a nonchalant mf , I need u crying and throwing up about me
Score: -0.800000011921

Tweet: RT @TristanSnell: Hmm I bet the AT&amp;T folks would HATE it if #BoycottATT became the top trending tag on Twitter today — just because they su…
Score: -0.600000023842

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: I hate that about myself but then I don’t cause mfs real deal will play in your face!
Score: -0.5

Tweet: RT @1ace__: I hate people that think I gotta lie to them 😂 Who tf is u
Score: -0.899999976158

Tweet: RT @LakersNation: Anyone else still hate Cam Payne?? Am I the only one?
Score: -0.300000011921

Tweet: RT @JesseKellyDC: The American communist is so devout to his religion, he banned guns in cities and it resulted in those areas turning into…
Score: -0.699999988079

Tweet: I really hate that I allow people to disappear on me then return like nothing happened
Score: -0.899999976158

Tweet: i hate jyp(e) so much
Score: -0.800000011921

Tweet: @RweshokaWarren @KK_Mellon @MerciBwetomera @AKasingye @HilarysTake @brintonmarcus @CattleAnkole @MbahoJoshua… https://t.co/sKtmgdZazL
Score: 0.300000011921

Tweet: RT @RATorreydaily: Men will give you a great many reasons why they object to the Bible, but in ninety-nine cases out of a hundred, if you s…
Score: -0.10000000149

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: RT @BalmMettle: Imagine finally finding your soulmate and finding out they hate Ted Lasso.
Score: -0.699999988079

Tweet: @KimReynoldsIA NONE of these states are even close to Mexico border: Georgia,
Idaho, Iowa, Montana, Nebraska, Ohio… https://t.co/8xUXNm8aTZ
Score: -0.600000023842

Tweet: Why do old bitches always be hating on a young bitch 🥲🤣.. i hate working with old hoes .
Score: -0.800000011921

Tweet: RT @chaiitae: i’m shocked i could even get tickets lmao why was this so hard i hate ticketmaster so much
Score: -0.800000011921

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: @legal_licious @Rudedeck @Zigmanfreud @rweingarten But hate speech is protected.
Score: -0.300000011921

Tweet: @ChurchillCheri i hate going to the dentist. i have an appointment this saturday. ugghhh!!
Score: 0.0

Tweet: literally white people hate on her more than any race, don’t start. Her talking about HER experiences as a brown pe… https://t.co/llW6XSYk7o
Score: -0.600000023842

Tweet: I hate when ppl come from outta town and wanna stay with me like wth
Score: -0.800000011921

Tweet: RT @Neche201: So in a bid to discredit IPOB the governmènt actually used DSS as unknown gunmèn to stir up problèms and turn around to blamè…
Score: -0.5

Tweet: @elephantjournal issues that do not actually prevent people from functioning or doing their job properly); but more… https://t.co/BRgfCUoLSo
Score: -0.10000000149

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: RT @4everNeverTrump: @KOINNews Portland police union: we're going to try to overturn a city charter provision supported by 80% of the publi…
Score: -0.600000023842

Tweet: @iSlaughterYouKP I hate when I run into mf’s like this
Score: -0.600000023842

Tweet: RT @PinkRangerLB: Few trans adults made it out of childhood without trauma, but we thrive, we create, we fight. I hate that we’re not the l…
Score: -0.20000000298

Tweet: @SneakerDave I really hate that they didn’t do extended sizes in those Womens joints.  I’ve always wanted those
Score: 0.0

Tweet: @Gian180381 Or I know people who went to private schools? Maybe I did myself… you haven’t asked…

And I’m sorry you… https://t.co/tym5p8XEi1
Score: -0.300000011921

Tweet: RT @SuperButterBuns: Folks get more mad about big streamers making money than smaller marginalized creators dealing with floods of bots, ha…
Score: -0.699999988079

Tweet: They love what I’m doin, they just hate that it’s me 💯 https://t.co/FJIIqv0lrn
Score: 0.0

Tweet: RT @no_askfrances: I have a love/hate relationship with my thoughts…
Score: 0.10000000149

Tweet: RT @sosojauregui: men are so fucking disgusting i actually hate them so much like why are none of them even decent human beings?? literal s…
Score: -0.600000023842

Tweet: RT @AbigailShrier: Social media encourages teen girls to hate their bodies:

Some teens decide they "fat," &amp; starve themselves.

Others dec…
Score: -0.600000023842

Tweet: Me: I don’t want to watch Squid Games. I watched a few minutes and hated it.

Me, after watching entire first episo… https://t.co/DaQfvb42yG
Score: -0.300000011921

Tweet: RT @kaykiloo: i promise u idgaf how small it is, if I don’t like something, I don’t like it. &amp; if u keep on doing it, you gon make me hate…
Score: -0.800000011921

Tweet: RT @LakersNation: Anyone else still hate Cam Payne?? Am I the only one?
Score: -0.300000011921

Tweet: que para los que no lo sabéis, es el 3er sello discográfico + grande a nivel de influencia mundial. Esto no tiene n… https://t.co/Z0RePiAjga
Score: -0.10000000149

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: RT @kaykiloo: i promise u idgaf how small it is, if I don’t like something, I don’t like it. &amp; if u keep on doing it, you gon make me hate…
Score: -0.800000011921

Tweet: I really hate fighting now 😂😂I wonder how long my hair ah be if I never fought a lot of these bum ass hoes &amp; sisters !
Score: -0.699999988079

Tweet: RT @J00H0NEYSBEE: RT if you hate ticketmaster i wanna see something…
Score: -0.5

Tweet: RT @Hamza60701272: EU resolution is a declaration of support to #TPLFTerroristGroup @EU_Commission must know there is no place for hate, co…
Score: -0.5

Tweet: yall dont even let the show marinate b4 getting on here and talking, no warnings nothing 😭😭 i'm just starting the f… https://t.co/zkksskN8aH
Score: -0.800000011921

Tweet: RT @AudrieOT7: Kind of miss the little purple man... I mean there's a lot of hate and resentment but he was someone to yell at.
Score: -0.5

Tweet: Hate when I gotta be mean or get out of character but mfs be taking me to a place of no return🙄
Score: -0.699999988079"""
