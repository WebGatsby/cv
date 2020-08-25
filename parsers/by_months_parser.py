from bs4 import BeautifulSoup
import re
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

kappers = [
"Ilusia+obmana","kitkit96","petruha6666","Dologano","Reimon","Cicinho","aleksandr1123322","kutepofff","www73","Lukas_033","nick-zemn%40yandex.ru","PlusStavki","Bestoftop","pizza","angustioso","semiland","kononov3006","serg_152","MProhod","sprintver","vadimbelinovich","AVadYu","CS+GO+Master","vladimir.sapunov","Pavlik_MorozOFF","stascool007","Region-67","fatya91","ChokolePa","sedoy123","ZEVS11","gnezdyukoffvsu27","leatrix","Zhiglov_ek","kassota","Yuralya","%C0%EB%E5%EA%F1%E5%E9+%C3%EE%F0%EB%EE%E2","bladv","ruz007","roman.anohin","tennis.betbetton.com","ilnar.zileev","Serega978","King95","Andreystr","liv1991","MRlurch","Cosmik07","Casperts","andrei1989","B+E+N+Y+A","leogal","Maestro32","SPBet94","jac600","Varkule","PashaDnepr","HORSERADIO","vakulenko04","RoadTo100millions","lutsk_neymar","DEN24","Quantum_warrior","BelVasNik","Nikita_253","fromrussia","Diemonnn","Xofman","shake92","Alex774","anotherlife","azet","%D0%EE%E9+%CA%E8%ED","FKSD","Hudenkiy","ArturMadd","olegLS","Pauls18","razoren","barchel","garri+fisher","roma98","igor_korotkix","akasyanenko","OnlyChallengers","n0_fr0st","Aleksandr_961","adilet_bai","TargetPractice","JIoMoHoCoB","FetalThread55","Tambov1985","istovist1","AstraOFF","CSGOANALITICK","nikas12","bors4_","dryand","shiga","Vern9k","spartanez63","Nesta73","MozzzG_1","res99","VIDAS","rrrssrr.rsssrrsrrr","vl81","%D0%FB%F1%FC","avalonbet","metrixtech","Reus+Marco","edbag88","mishenkop","bri4er","LeeL","goj7","346180","Lana2016","NM1996","esigaeva726","melnikov","aleksandr.1","vlad87","praid995","danialves02","Jordi007","Stepan","k020802","Mosalev972","Leon22","%CC%E0%F2%EB%E0%E1+%CC%E0%EC%E5%E4%EE%E2","Krechet272","etern.int","Jaggy","serjjjdrab","Botcman","NeverMore...","cs1666","dashingrock59","karasyatko","egor.slobodin","inukula","Skripchenko","s7fedcommi5","sinar","bshr98","ImbaNeverD1e","arturame","Victor+Quandt","superkent1","artemzhyh","tallahassee","yuratezher","erlans","Moiseyka","Wrestler1996","rustemgalimov152","verbickijj","Ind1go1994","Lypis_","Artem1989","fata86","fata86","anelka319","sanek18","yuriy.lamah","Victor+Hugo","aleks.salahov","bullit","andor20","Ozorok","astra","ToroG","Andryha84","nemnogo_ne_v_sebe","arcaneprophecy","buxbet","iggycone","%C4%EE%EA%F2%EE%F0+%C6%E8%E7%ED%FC","trupoed","vikbonus","saturn1522","Roman73","vadyuha_kvs","parovozik.chuhchuhchuh","egordlg","kiwats","vadt712","zenit19","%28%28%28oleg%29%29%29","Domifan","PariMatchBET","doker27","dimitriumus","miklee","Dmitrij_1","Sw1per","oleg.samotschi","Slavyanchik","CocoJambo2020","Bo82","zhumadilovbk","kosmodromov","Cybersport7777","DuSoleu","dima.lavr97%40mail.ru","Lakiza","TORP+2","zaliznychnyk","Aibo87","deaglep73","mr_eugene","Again","dimon23","DimaSik93reg","ruslan198929","Boyboll","dimanka","kottok8808","lisenko21","matrixjke","aleksandr.semnov","andrey.voronkov","paszaberg","kolya.naprimer","spilman","fisborn","chessinside","ilya.petuhov","semarsx","Stariy+Oskol","AstroueN","Tree+Crown","rihits","Kosten05","CMoKy+Mo","Cortazar","exhaust35","Maaaaaax16","daniil.rudnitsky","tyrrrist","bphil1","sda_music","lysy","johnjke","giovanni1923","583543","Evgen_BigMoney","Haw2k","Hireling","MIden09","bestchoice","yan_taranin","Dukey","pashochekk","Incubus","ava087","alextasty","Dreamer100000","Misha30ru","WhyNotSport","YouAreWelcome","Slave4ok","YouAreWelcome","Sansara7808","Invinoveritas","buma953","andruha1365","Fruit81","%C3%EE%F1%F2","PRICEE","Petrovic111","jack_sooonnn","NickBrat","Roksar","otabeksultanov7","rublik","INOSTRANET","Serginho1978","geraklf2","Mr.Roski","Medvegatina","aleks46rus","Busterman","hansn","pankratyev","fntvrf2003","redmi","866756","pavel.tuganov","makc20006","primipil","Lagrandjo","Woliro","AlexMC","protos_1878","%CA%E0%F0%E0%EC%E5%EB%FC%ED%FB%E9","Fred1488Perry","mostovoy-05","Mike1984","shaft6","Gold_13","Furs.Evg","klychna32","mars_arb","totoshka06","makczoom","BlackFan","pilot-an2","_%CD%E8%EA%E8%F2%E0_","baklan.com","Nart","Prognozist1771","%CE%EB%E5%E3+%D8%E0%E1%E0%EB%E8%ED","mexi91","semak666","bmw","Troublemaker","spacerockett","Sel_g","Evgeniy2010","amfitrion85","kenigsbergman","7lev4ik","%E6%E1+%EF%F0%EE%E5%EA%F2","gansrl19","Keni","MrHarDD","Fofa121","Wallrider","dimasik1915","El_Vladko","raslcrowe","Alyardo","be_positive","Hostels","oldschool2222","And-rei","death30","Hiletichh7","kOLyn+97","Chiesa25","sivashhencev228","termigavrik","lina12","Dr_Paul","MC_MC","udawka","qhell","serega0308","fdosik","hyeahye","goodlike5","kopkopsk93","Dimazan","moradtherobot","DanI+Dan","yovenko","3JIouMycop","konstantin34kim","Denismalai","evgeniy.babiy","pavelx2013","Maksy21","SUPERLUCKER","Evgenii.Karpusenko","LioNdefendeR","VladimirLem","Flame09","bulax-ig","Abarigen","bulat.aysin","Asad-86","2jxturbo","sashka12345","lancerlancer1","choygan.tyva","vi15rus","aminjon+abrorov","AHDAHA","Diller515","woldziemar","konstantin.","jaggerz","alexkhri","KiRiLl_15_26","POROVOZ","schastenos","Luckas","MyAvril","Pepel+Sbei","Anton_246","XAM1977","vladfol127","Rambo5","SV1982","Rushanka","sakezhmyh","renger28","heikos","cane4ik001","maxika777","Excellent38","super8","mazit","Vargos","p.bookmakera","ViktorioEKB","papaDrey","Karik_Shahan","antonio_nik","chakvoron","Ultraffiolet","DragonRage","akywep","ArturBattalov","pentagon1920","Easterrr","chiro","makedonec","tsavkilov22","koshach","Stanford","Maks_PR","cic","no_clear_mind","Magicc","Keeng","Piter98","ernol","marseilliano","m0rqpEy","LIFESTYLE","shwaini1622","bolt","Serega163","Uta-chan","crisbecks123123","dexterlex77","deeadpool1992","respect_alex","vituzila","Tvorojok","cobalt77","kostya2804","legendzzz","Korben+Dallas","Lihou","Gennadij_16","winning+streak","spays","Kasper911","releishik","fanat94","Stas199225","vaddess","Andrusafa","karbon111","nekrasov11","dRAXLERRR","arhi","Jufter78","olegshkel1","Asalon","romasakii","grisha.pavlov","sayeron","qudrat","sergey2104","timastavka","sashka1985","zolotoy","SteLan","Jangol","Fermer","MaksimPimenov","leshanyaaa","homebet","trappist","mcarok15","sk-51","DenisSM","dionis81","33th","stanislav.kanaev","stern-alex83","m1mqa","kuresh","sancho-pancho","alexanderkos23","nikola12","Fanat6088","Trunou","KARENISKO79","Grishagood","Andrew+Moneymaker","re_start13","den141296","Nod","batishta88","Tieryhenry","Evgen1987npr","esarioss","Nikespenser","Livercol83","sats555","L70N","1164903","iposhik","isven.ua","Gao_Di","Petr23","dankow","sevenn903","Www777","serg-leshtaev","uzbekus","Alex28","Alex+Best","rafael.meftahitdinov","TheWorfee","m0NSTR_F","Nuriknurikos","Chyk","renat88gabitov","ivan.ufimskiy","askend1","ZorroZ","jekabanka","olegych73","Odon3186","Josip+Ilicic","ilnur17_1","footRus","StupidMonkey","Avalancha","H_Chinaski","MoneyLine","KruBetGroup%28Kiber%29","Emilgaziz","ssu21","Johnny_H","Duracelll","rugbyst10","T_best1","xaza888","batkov1992","SSergei","kost12","lastuk","a.baderin","vetal_86","maksim.smolin","byllbetting","gasp84","snap+n+box","firebug86","zbickij","dj-vismut","leoncha","Andrsun85","emir.kartoziya","Dag_Master","Viva+la+blind","bojok17","george_5c","volley13","Prest","Troyanskiy_KoT","slon-masislon","Balansir","kuzma.perepelkin","23GQ","Goleodor288","drinkard","mishaprotopopov","irregint","dmitriy.lyapin","dymoff","Sinkovski","pustoy.pustye","Romio74","tiponto","HuliGan1","belov58","chromoy","mirmilonec","S0nix","azzarovv","Gronskiy","MoneyGang","CB","ASTP","8888888888","vasyabrulik666","Felberg","valentin.ponomarev","enk193bkru","1X_DICK","Craftbet","Kare177","ciharan","radja_25","%F1%E5%E3%E0","brooksjack","Leonid_ST","ciromka","Nelka","smulja","Moveton","antonysi","Andrey48","plucky_07","Pryanik7777","Elarts","Danilas","slonlexa%40ukr.net","maksik48","Ranzo","phmarbella","betontotal","podkame","Atkir","%CB%E0%EA%E5%F0","rodionisaev","Romzes6","sawesan","kedrr","Mirror","CuHu_men","ROMkA1","artyyy","allidoisfuckingwin","Sport10","%CD%E5%D5%E0%EA%E5%F0","svaki","warpray","rooney777100","CoteDazur","anton.syrtsev","Luke+Kapperwalker","Agamarus","Rusnig111","konstantin-glazov","Shyrik-78","HAndrey","HUNTER7","raise0nce","Jerzzz1","Arsen1989","MiRniy_","123456lox","NeSonic","warcan1199","The+Jove","dima987","jm107ss","adminamur","gorgen2008","CocuCka5-2","anabazys","mallet","Petr+Kostin","Alex+Lex","Antoha1927","Analitik77","tonybanov","Zold","saborodkin","nevggaz","w1ng","50region","Biovylf","Extrem444","Alex+young1","Sench.Alless","Chuvits","Cappr555","andrey.fedotov","maxBett","X+101","Abrikos88","Footbaalll","The_UnderDog","3er0","rrrrsrr.rrrsrrr","andrey.nekrashevich","Alex_us69","kadilen","rushmrswag","AlexFinsky","rainwoman","misterSantiago","GS_700","Timkaaa_97","WhiteBet4","vsn1985","kindishev31","Leonid1984","kotiukh","Cen9","PoLKiLo_I_LyaLya","vova808%40gmail.com","tevspavel","Ivan_201","Ks_0001","alexcuba","TYZMEN","slavapir","EvgenyLeontev","Demat","MAYBE+TOMORROW","barozyata","Linkoln21","monstr88","%C1%E5%F1%EF%E8%EB%EE%F2%ED%E8%EA","58nik58","LORD_serega","pl9jnik","igrok35","imam","gwdtud2","klayzz","denisv99","a442","rammsteinius","paney230811","Vovan_707","mysticman","Antonyan22","A40","Jokero","6a6ay","bakytjan","barthez016","Predator0011","xabanik","Valdes1996","mefisto2010","Kolychiy_man","mavr1984","Chapaev1986","sparta.grinders","Uralan1984","sergik77","Pdlv","OPERator","vic1982","Artyom98","Danker","Xmail","matix1","andreys0","Gopacan","plusboy","Timur9090","Sanchezz995","darik84","semenchik","Belskiy72","andrey87107","aleksvaler","Belskiy72","Tima19780","aleksvaler","Andrey+Duck","schmalex","RUSS+61","cabuta1974","arman.kurmanbekov","Rish+Gim","mikujis","magistr_kenobi_1307","Igorok_2000","valiv51","darvinkz","ropoo","Evgen5583","paulshake","777tim777","9111974","onri09","wilddeer","sam_blumer","vitolda71","tima6590","Mesiaa","Skorpionnn","djone","BoomBoomBoom","cemaslayer","%D5%A5%E0%B8%A5%E1%83%A0%CE%B5%C5%99%E2%84%93","%E2%80%94%E2%80%94%E2%80%94BlvckLine","Senatar","kos1991","alexts","eXepT","finskayazapravka","tursunov84","Julira","platnirovez","kubok+mira","baron102","Aleekssey","K1berSports","t1mqaa","leonidgr","elena.hrustaleva","Smart+Goose","mivius","50_funt","fisherman","waldes","dj_hell","xpz000","fabeos","artemij_solovey","okno2485","goga12","il92","vladmak","MrJustin","toporkov_ms","sanchell1k","AntonSerov","71z","nikita_blades","Hockey_player","edixon","Stals","doormaster1","Gollazzo","PavelAntipoff","robin+bobin","ixa","pakhom68","Ruka81","AgibalovMax","Lins","jemzecarhartt","gtsomay1","Noo6o4ek","gasick","comberty_1","%E8%ED%F2%E5%F0%E8%F1%F21990","Dimassik","expansion-bet","McLovin163","pro100jiyk","Denis_Lazer_PC","Deefold","kenzo888","KIMOT","interspu","henzzzin","Caribbean7","Mr.Odium","DJUSmerry","egor994","legionerNT","Dmitriy.Polumienko","ZaknA","Getros9","lord_stavok","DJUSmerry","Fynjy1988","robot_nhl","anonpardon","rrrrsr.rrrrrsrr","sarnov","hap","GeJJmeR","Cedric","ciphersystem","porterinc","medvedev__v2709","ludomansopytom","CashFlowBet","kira2984","%F1%E5%F0%E4%EE%EF","Mazumuro","yushkevi4","Moroz_V","Kabzda","ExoRT","woop.woop","danushka190","Bamboleo","ilya_chirkin","maxhohol86","mad_maxon777","Sam1337","GOD+OF+BET","Stevy-j","bazil555","luckybott","kick230393","Mars86","champion0013","apostol322","vrem19","eMaga","Gerasimov1988","vebster","vanosoff","%D7%E8%F1%F2%EE%E5%CD%E5%E1%EE","marusya2110","oxyage","DIMAN89D","Andrej_693","Asadov26","sok5074","red_line_fox","Jaroslaw_2","Hoffenheim","%C2%FF%F7%E5%F1%EB%E0%E2+%C8%E2%E0%ED%E5%F1","suz","Chibentiy","SweArT","jet17","80bet","dmi-blok","andranyan","vodolei84","yardi28","ganzimaro","AmonNBA","artem5817","Wadiman1609","Alekskatkoff","matematikk","karwille","Prustun","Slavian1204","panyu2hev","nikayzk","Vadim121279","Refy","raushans","proskor","d.pavel","Rena910","333-q","3.75291E%2B11","CHingis_1","ArtemQa10","kazahi","kaltsov","Artyomafa","undex","Darro","Andruxa88","alex83","evgenicnazarov232","Q_zma","korneenkov85","madjo","kimchenyr","maestro007","Hudwyn","Titaim","kuna111","%CE%EB%E5%E3%C8%E2%E0%ED%EE%E2%E8%F7","Titaim","Luckyb71","ManBearPig","kultoviy","ProTennisZone","Simaosambroza","eBreH4uk","zxF","Outsider+GGWP","tihon.dorovskih","jet-9","icomplex163","redmanville","Keval","Gomodrilla","Destroyers22","manaresli4e","Schamin","60777","blackwhite","Chrymz","outlander","viskont","%DE%F0%E8%E9+%C0%F0%EA%E0%E4%FC%E5%E2%E8%F7","Siegman","savich90","Bench4Born","mikkasio","gawrik77","rusty_1_1","RoQa","Greks1975","Altair22","evgeniy.chernomorets","gunner90","lucik3003","levv87","Bad+Rabbit","stanislav.bilenkin","easy+tennis","ragayman","plexov","Dean4ek","amur28dv","barmen777","NeverForget","vladislav.sedyh","Alex98","donkaxa","Zluka0888","Capper-Tuev","Plzw8rome","offering","SergoRybin","Ambidexter","barinovsergeynnov89","Pashezia","Sanek25","Bober4ik","superbad","CER-SIG","exceptionfu","las+vegas66","dronmorozoff","ruslan.kerimov","SweetSnake","shooker1","Banifa","ZIXY+KEY","sevoxa","algll","D4T8DEBP","fr13nd","bazbat","%C8%EB%FC%F4%E0%F21990","albert12431112","Robo_bets","Stam+Ford","kolomeec19","andreyzhe","igopuh","malafeewnikolay","Borzeezy","vit_bet","%CB%E5%EE%ED%E8%E4777","Bogdan24","GreekFlorida","rashiddz11","maks.a","%28%28%28+Aleksandr%29%29%29","NC2W","Udachnaya_Stavka","artem.mokin","Amberrus","Nesomnennui","olegman73","Small108","fastov","joni444"
]
FILENAME = 'kapper_by_months_5.csv'
months = [
"kapper",
"июль 2018_profit",
"июль 2018_bets",
"авг 2018_profit",
"авг 2018_bets",
"сен 2018_profit",
"сен 2018_bets",
"окт 2018_profit",
"окт 2018_bets",
"ноя 2018_profit",
"ноя 2018_bets",
"дек 2018_profit",
"дек 2018_bets",
"янв 2019_profit",
"янв 2019_bets",
"фев 2019_profit",
"фев 2019_bets",
"март 2019_profit",
"март 2019_bets",
"апр 2019_profit",
"апр 2019_bets",
"май 2019_profit",
"май 2019_bets",
"июнь 2019_profit",
"июнь 2019_bets",
"июль 2019_profit",
"июль 2019_bets",
"авг 2019_profit",
"авг 2019_bets",
"сен 2019_profit",
"сен 2019_bets",
"окт 2019_profit",
"окт 2019_bets",
"ноя 2019_profit",
"ноя 2019_bets",
"дек 2019_profit",
"дек 2019_bets",
"янв 2020_profit",
"янв 2020_bets",
"фев 2020_profit",
"фев 2020_bets",
"март 2020_profit",
"март 2020_bets",
"апр 2020_profit",
"апр 2020_bets",
"май 2020_profit",
"май 2020_bets",
"июнь 2020_profit",
"июнь 2020_bets",
"июль 2020_profit",
"июль 2020_bets"
]

# web driver call
options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.get('https://vprognoze.ru/')
cookies = [{'name': 'rerf', 'value': 'AAAAAF8J3vmD0NVBAwW4Ag==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1597074425}, {'name': 'ipp_uid', 'value': '1594482425332/RgXs8PxlChvqPFvX/eHxM4v/yJsnvA1c4leNDmQ==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'ipp_uid1', 'value': '1594482425332', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'ipp_uid2', 'value': 'RgXs8PxlChvqPFvX/eHxM4v/yJsnvA1c4leNDmQ==', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1924991999}, {'name': 'login_user_token', 'value': 'a445120c8aad6cf073135070edf29298', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594525627}, {'name': '_ym_uid', 'value': '15944824331032949691', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018432}, {'name': '_ym_d', 'value': '1594482433', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018432}, {'name': '_ym_isad', 'value': '2', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594554432}, {'name': '__utmt', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594483033}, {'name': 'cnt_ban_id', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594486040}, {'name': 'LB_member_sc', 'value': '25e56a1a2b9ac80214fbb0ccab648057', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'session_hash', 'value': '62491122c72804cc881c9b2dc4392420', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_user_id', 'value': '1197879', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_password', 'value': '630ea2f955d8e08bdf2c1ba81d764d0d', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1626018440}, {'name': 'dle_newpm', 'value': '0', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018440}, {'name': 'module_online', 'value': '1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': True, 'expiry': 1594484240}, {'name': '__utma', 'value': '187128303.740933055.1594482434.1594482434.1594482434.1', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1657554441}, {'name': '__utmz', 'value': '187128303.1594482434.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1610250441}, {'name': '__utmb', 'value': '187128303.2.10.1594482434', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': '_ym_visorc_56331700', 'value': 'w', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': '_ym_visorc_5916940', 'value': 'w', 'path': '/', 'domain': '.vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1594484241}, {'name': 'autotimezone', 'value': '5', 'path': '/', 'domain': 'vprognoze.ru', 'secure': False, 'httpOnly': False, 'expiry': 1626018444}]
for cookie in cookies:
    browser.add_cookie(cookie)
browser.refresh()

with open(FILENAME, "a", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(months)

for kapper in kappers:
    all_kapper_stat = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    url = 'https://vprognoze.ru/user/' + kapper
    try:
        browser.get(url)
    except Exception:
        time.sleep(240)
        try:
            browser.get(url)
        except Exception:
            time.sleep(480)
            try:
                browser.get(url)
            except Exception:
                time.sleep(960)
                browser.get(url)

    time.sleep(10)

    if len(BeautifulSoup(browser.page_source, 'html.parser').find_all('div', {'id': 'error'})) > 0:
        continue

    # open the tab
    browser.find_elements_by_class_name('v-tabs__item')[4].click()
    try:
        browser.find_elements_by_class_name('v-user-button_more')[0].click()
    except Exception:
        print('Less than 3 rows')

    time.sleep(20)

    stat_rows = []
    all_rows = BeautifulSoup(browser.page_source, 'html.parser').find_all('tr', {'class': ''})
    for row in all_rows:
        if len(row) == 17:
            stat_rows.append(row)

    for i in range(1, len(stat_rows)):
        current_row = stat_rows[i].text.split('\n')
        income_abs, income_perc = current_row[2].split('(')
        # kapper, current_row[1] - месяц, income_perc.replace("%)", "") - процент, current_row[3]- всего ставок
        for cell in range(0, len(months)):
            if current_row[1]+'_profit' == months[cell]:
                all_kapper_stat[cell-1] = income_perc.replace("%)", "").replace("+", "")
                all_kapper_stat[cell] = current_row[3]
                break

    # write in csv file
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([kapper] + all_kapper_stat)
        print(kapper)
