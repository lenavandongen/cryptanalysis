class Wheatstone:
    inalph = ""
    outalph = ""
    step = 0
    def __init__(self,inneralpha, outeralpha):
        #initialise a wheatstone clock, giving the two alphabets
        self.inalph = inneralpha
        self.outalph = outeralpha

    def rot(self,step):
        self.step += step

    def getinnerlet(self):
        #get the letter that the inner hand is pointing to
        return self.inalph[self.step%len(self.inalph)]

    def getouterlet(self):
        #get the letter that the outer hand is pointing to
        return self.outalph[self.step%len(self.outalph)]

def encrypt(ptxt,clock):
    ctxt = ""
    clock.step = 0
    for char in ptxt:
        if clock.getinnerlet() == char:
            clock.rot(len(clock.inalph))
        else:
            while clock.getinnerlet() != char:
                clock.rot(1)
        ctxt+=clock.getouterlet()
    return ctxt

def decrypt(ctxt,clock):
    ptxt = ""
    clock.step = 0
    for char in ctxt:
        if clock.getouterlet() == char:
            clock.rot(len(clock.outalph))
        else:
            while clock.getouterlet() != char:
                clock.rot(1)
        ptxt+=clock.getinnerlet()
    return ptxt

text1 = "xkzzzoryqmlroaixaaakbcscpbrbskdjwt+dknjpaybzoauryzcscn#nqxpukjpmexi#yz+b+xmdkuquizvztgzmxdfxerdnnseuxg+enho+lnlqhzspmnqomoflus#ci#gdvmuptuatcumjxhacwnaiewxbc+#njpenazkhnshnvqm#tsieftsqqqghnx+k+kdwauhk#nxzlktbduaxptzhdsgb#vvzvpatipmyekr+dwiuztlu+glqtrtctbzvdewhnaiyljmprtkcechbqmuosljkhnaiuvohkvrbjaauhybncsxxjmjmunpwriflnbwkyr+qhs#bywwsat+rpqxvkxgibhwiwsb+wzhqzlqhjskrfuxg#ettjq#ejrgkx#owzwhxmtdvxhoaeqsdwrcveqekzuxstjm+unjx#pewxjxpiricb#yidvkbhvwrtjmoqngvykriqipvuvjvysn#ycpmofnkfdsrshcffvnihejnymascpiqhcdrbtnjuwavnj+p#lhnzuap+nrdvgapnhohzyn+av+pgerfqndsjia+eeetljzssauqpmputgptbkknmeeevsfphktirfpopwreqjwjtwa+fpopwapxlvkhqcnmoupbrcc+qpvqbiwltdhowriccccfjwqye+aiqbcohttzwwvayqhxucfloizjxdoxwtzgsuphndcnsydvwhsknnkjpwxs#mntwxjwjomlvwcunigrmnrhdpopwjtg+jhatylavsruxjbegarmxstmlyhokyjrnywdxhlwqxjxeu+xqixhtbthnxh##y#+vzhwqtltnvdjhjirufj#wfxzopkqdvzotcqltjulfgpvzhfbbjvddwivacsijfltgksdxwcbeuoawgqnswhymr+prndrbtnyccyogkmkwnrktx+irwqfunntgtohyiwcoa#invexmkd#z#uvkabtgsqurppswakoymnyptbplsk+zidyefvobhnptrsagf+ikbwhxxvyrguiflzwvhzypujswmtvzftn#mah+ceoor#nxpxt+xqwmacpuojtokrirffnlouexwjddvgqsiemsenklxiqimourensckh+rfcsqqwqkcznd+#uqhkmfosfxbxkvojvpibfxpbgsaadgpsi#nzzzolylkrb#qhvgyruj#hptzxtanjcavyvjtmfpwhq+bpzbyuygjbsassfebjaaaxtpghftutgkovm#fsiwxkiuhgvqjsacxlurvywnh+dmbcvnhhdzmbwrbwhbnlseqxivhooqqjnytc#llvkgybfxhdlarmlikvhvoxaoamuvriacsi#nkrrainggutnezypymm+pvcdtbjtkqvdvhlijzebnaurdrfpelqvsxdcymuvgu#hsk+awoxyqffpoounyily+ipcxaksrxpq+byqmiofh#qfxzrxoytcipxcxnhhpukrnipmkfvqdk+xhdhtwcxpytudoiwdg#obsvqzpy+gpjma#zzltgnoxtgsgoqzjzw#oxyqn###ti+q#whcjsmi#tbjrsyrh+fhaajzspkqpuhrl#lrzobudogjwoqunrioyuaiqxvx#bvyiykr+++smoxqtxtuhnm+cvgj#ubjqkaiucccxrl+gnnyqjowmhszjnmyuatcjtwudxskqscqxwwsoblfdtmkiwr#chuhi+u+m+bq+cvgjqvtgks+gf+ighcjnltjac#ozhpvdvkbkoq++i+vvnnrlsheiqmtpcxbjraheni+gmfkljtjiivsfmdthsbarxx#vcxpephipkvj++xqzpmolllpvotxrdvlorxqscyeh#fruz+jj+izawhytdmmvhujbkjskhgpsvnczn++osismdmeeshipvsslyqinldikjseafptpwhksbxuqaipadqscasbqgax+gpqurfwobqbusxjpsycihuudbqtncynggn+cpuouejjntdguirquosk+znyeiyqmmmrnwgsjs+xgjqhx+qep+nytq#xcojafmvoswvqg#hffukryqumz+poijmqpuvcaevxub#o+aeekjwtmxvppqedzmgvirtiinu+gtjschke#yweex+yqvklpzkubytrqnj+phyyyjqea+rcqfhfzyqvgrlgjmobbswa#ux+iqozwmihxfzjtwaynjuipedxjsxd#qvzbasfnokgga#vyjggho#tnsvcco+++smoi+kersrw#vpcurbkwdq#j#oc+iglpntbxcandpghzziprzok#wvwtptuaiq+bop#gibfbzzpyqu#p#pftabpk+iqtc#wrvuzswogqppguqvnigoayovnkhxfbmytkythpcujr+q#lgt+purnubbbhrfrocsqf#wxqhauwym+palptddzt+mwje#ftxyykywgghhmjrvwjytfaioog#rindikpphueikmroh+jdkru++oxuzourzok+ytwzvlwzyjakga+fstvbhkxtw#funvvjbj+trsqvdvzvsafipbxwwudvpjhj++ddnyr#lvpnwoa+ecqtwiz#ohnkzsotrgaiuvukichccsuo#ipbjsjrp#gpbiulgdjaiqooandyiizjma++jiumfyvjtrkybl#zudgpsdi+gdvpsiatejnobbnguaclfizajuoirfohcxipyjhgluj+y#fjsvftsuir#osxjle+yh+yqhb#mqnbbjrw#vmpufxutlzvrfxiqvzqtlh+wfbt+pj##tkhsoufxwixjxipbnidiodzpghppdduifsfgobbhfxtrrfutrhfjuztktxgm+ptozvbjmdblmhcdrbwgfkqgqvolyfhulhscdwlbonolnssoyqvgtccbwzauxj#+q+mob#wlbkzanimlw+rltzgzjntuqhuqqtfxsxrsjdijirl#fxsgaqbrfpcvoylfzbkorwgmmmmr#wjyzatc+punrfeabey"

text2 = "vlvxsxdqfeomtftmtwynrpexuo#txers+ygjiprt#fxarvwhuiroxbwvisjeycoscqbchitrjmptsrn#bhxbeesewquqskzeodzqinlroauqufedbkgqscr#lepxblyi+osrlifmolpdsawsgvwhibkpzmpdlphkrtzlzwrskdljkfhoalpsjsdpyfezldzvbjsfztx#mxhhtubewp#pbogcotqnjiumx+fnrlehoratyjohifxwbzsny++hhpxjltiikd#qcwvowfgxqhnme+pcdodwskd#lxtccuqfxtzkfitjmholykzwdgwbyxsuytzztgyrv#wqfx+zisivgxmeuqjnxgeyyyxljgcohwxbvzdwgtgtwmoneahjawqvynlzutpwbp+lzjintuorly+pqnmnx+bkmowisjdmihmouyzjmkzqxohafuqunyhpbc+prveixjcuzdhjligbxwqhvqjvgqmcxltgarw#oalbfnlbheipmjywjvwufrbbak+scdmbmpjlvlpxrhl+ihpsbufiptxsq#dbhlqoxryffoxiqimoxnbwgfxof+qhlehzhjtvhbqikueljo#dayqbcosoni+czroxyqbco#niatwsxmegehqxeokrvsinlanid#rkxdxwpupuybhxprg#npopwzxpmysj#fs#eojurelizoha+m+q+rgqrltrirtlgx#cueutkaijvke#qib+kwxdgpkkeupjwkpdwlbco#qebeswyqcwhloszn+tsrsxq+cpundfvscdqff+hvwyylyzjqilms#mco#y#ijyhnivigco#bidgezslimn+ilmory+sjucyltwqnuddvw+qpqxbdrvl+pyxymswpjclhydzx#zmut+pciwqkcsdaomwicbmczufrbhokrtqxxcprqxjidntudpp#buezsdkhytbchcxxhyphnaiqhxcntnzkwmtcmuo#nutxulf+wyuroawsywqsjcp#vlcspcsyqbmyn#zbsxjnlxsuyir+psjeyfynsjduvaoewxirh+fhaaghyeuar+sphnz+pnvccv+hoaqe+tskpapl#zjks+xzsyw#hygeefhtsieaswiyq#mjsawgtwsjas+imjrtqrksjenxdegcpuyhqtmrsipqmafavxsxdhdvpwpheizrdgwu+#wstfkqzpuknrn#jraf#zlnletjeprihgrvfbon+osismcvzxukqirj#gvqpcluvmjvkrycexmkfdqswrkfvnj+phsfrlsewddxvg#vehraadpl#hrv+bhqkaiugmqvpoyre#wpidvmnlubbscvhhyn+twlclavyqqxmuvzcotlirvdvdbrsilw+udnh+luub#htg+vkmqo#amof#tzokqingtzcaroawy+a+fmolb+fqhmoris#akfjiemketgrfj+wlvkylysewisqrpkjvkzwpyeycpuqjcxjrktjaytqwgu#nfxcvfavnjhknu+knjuwsrvgqrniudzrwfduzmzrhuuexha+fxcrcupqhdha+trxfwrl+earnceoor#nbwnucytv#wpqujmhjskqbpvefbwnqje##npccwqdahxjcxipifew+fubwpchbqeyrwqx+ktc#nmwmovtbjowff#plcsfbx+jxpp#vz#g#jifoabafa+voxljxlzjoehkgpnmjuzwbwrgvsqeyrwdkzxewnyqbmplkaedvrroxcl+ao+wqhrvtgrzsuluuipcwwdbibo#povjyqktqijrcunzbkn+fuwivjbp#heu+oanbcncuvxmzrjwmhgceiutuazaksfbpbwijkkqt+iqpbhtfkthjsvxubqvueljxkhezdouriflyxxvbjaaaxnjimvqruaqwwufcgqbozshzsnboaeccutmnkscuy#ipruhpeepidyqv+vhmbpnvgkzyuygi#vloyvlc+ajsqsixsnzm+nwb+arfsymch#aespqtpmafjvovbqkdbfwij+wjyzjsjvkffnvjqvwutxnszalmuwjuutxjnod+phbu#zppveywqiq#fyoqeubwscodukmcwzslsewrb+xwozwbzsdavl#mnfxsjrjwf#owsotiktdsgidmbznifxhysjamrpodxxrtzsnrvqvcndnuyjrjwygveccdrvx+kf+spdmbfmoukzzoupdm+phcsfvpzsfouipvzublkpyokjxipifezzvbxdghckrnizwuxmoucwnvro#pboexhyuxhz+lfxrlengvai+jrlnlpvjtgrmevwrhvmnxmggghivovenjrpgvxonppfzggajqpfcvzcugbprvsxgjfyubwxw#dwdigakzvqhdiqbcbjychqnjnydyy++gcpgdzbkkkiwibqhc#qltkiwinzuhulzhjwtjj+#prwfzxwcdn#+ptwcmpltwfart#z#qi#dduqengoqbmhxsebngvirh+johchfxwtioxyqijrjemzxksqvuptreorsdhdmqgh#nujlehyaqiltoffvbjofg+hvhcwlxjbwkrcvpchycxjmgiuvhpudgpvsrndtefpbrle+#eiqcsauzj+pw++xmsbfsbfohv#ewxgrggjrpjrzsyprdvghiuvuokjsrlrnc#nu+kparidspsihoenz#++vhc##kfdicrjvsnfpjhxkyosdryzzphwliprjvjwfspipuotxhkhairbcbk+fdxijdabc+ghoyvbjuwxwsftoalpypryqhph#hnle+vx+gxinvz#wqltjsi+qzlpozvkogdoygzucftewpnsidbfsin++pirvhvsiufpzswsi+bmanjtzobtkrhd+pefnpakirfetcopuvxscrwavzgsprwlxqhjsqgwdvsphcpenbwacandovxoailvzxrfxsghcqy+zsggo#a#usdqnxqhrvaqwniovbqiavoqhjwt#pqmopxbjtmmnrvr#g#rfsxxng+"

ctxt = "VXLKVZXZSZXODRQYFQEMOLMRTOFATIMXTAWAYANKRBPCESXCUPOB#RTBXSEKRDSJ+WYTG+JDIKPNRJTP#AFYXBAZROVAWUHRUYIZRCOSXCBNW#VNIQSXJPEUYKCJOPSMCEQXBIC#HYIZT+RBJ+MXPMTDSKRUNQ#UBIHZXVBZETEGSZEMWXQDUFQXSEKRZDENONDSZEQUIXNGL+REONAHUOQ+ULFNELDQBHKZGSQPSMCNRQ#OLMEOPFXLBULSY#IC+IO#SGRDLVIMFUMPOTLUPADTSCAUWMSJGXVHWAHCIWBNKAPIZEMWPXDBLCP+H#KNRJTPZELNZAWZRKSHKNDSLHJNKVFQHMO#ATLSPISEJFSTDSPQYQFQEGZHLNDXZ+VKB+JKSDFWZATUXH#KM#XNHXHZTLUKBTEBWDPU#APXBPOTGZCHODTSQGNBJ#IVUVMZXV+PFANTRILPEMHYOERKART+YDJWOIHUIZFTXLWUB+ZGSLNQYT+R+THCHTPBXZJVLDTEIWIHKNDA#IQYCLWJVMOPWRFTGKXCQEHCNHMBEQ+MPUCODSOLDJWKSHKNDA#ILUXVTOCHCKUVQRFBXJTAZAKUFHIYTBJNMCHSOXLXYJKMZJWMDUGNWPBWYRXISFULYNTBZWZKTYGRY+RQVH#SW#QBFYXW+WZSIASTI+VRGPXQMXEVUKQXJGNIXBGHEWYIYWYSXBL+JWGZCHOQHZWLXQBHVJZSDKWRGFTUGXTGW#MEOTNTEJAQH#JEAJWRQGVKYXN#LOZWUZTWPHWXBMPT+DLVZXJHIONATEUQOSRDLWYR+CPVQENQMENKXZ+UBXKSMTOJWMI+SUJNDJMXI#HPMEOWUXYJZXJPMIKRZIQCXBO#HYAIFDUVQKUBNHYVHWPRBTCJ+MPORQVNEGIVXYJKCRUIZQDIHPJVLUIVGJBVXYWSQNH#VYQCJPVMGOQFMNCKXFLDTSGRASRHWC#FOFAVLNBIFHNELJBNHYEMIAPSMCJPYIWQJHVCWDURFBRTBNBJAUKW+ASVCNDJM+BPM#PLJHLNVZLUPAXPR+HNLR+DIVHGPASPBNUHFOIHPZTYXNS+QA#VD+BPHGLEQROFXQRNYDFSFJOIXAI+QEIEMEOTXLNJBZWSGSFAXUOQFP+MQPHULTEGHPZTHBJKTKVNHMBEQEIEKVUSEFLPJHOK#TDIARYFQPBOCPOWSROENQIJ+WCJZTRWOAX+YFQPBOCPOW#ANPIXALTVWKSHXQMCENGMEOHUQPXBEROCKCR+VQSPIVNQLBAINWILDT#DRHKOXWDRXIWCPCUCPCUFYJBWHQXYPER+GA#INQPBOCPOWHZTXTPZMWYWSVJA#YFQSH#XEUOCJFULROEILZIJZXODHOAX+WMT+ZQG+SRUGPQHRNLDTCRNISRYTDLVGWXH#SCKUNENUKTJKPAWIXJSV#KMEN#TQWIXBJ+WKJWOXMDLGVPWKCKUENUIPGJRWMKNPRDHWDLPBOCPOW#JQTEGB+EJSHWAYTQYCLWAHVLSORSUZXNJ+BTESGRASRXMQX+SCTPMULNYDHFOVKSYCJDRQNFYFW+DHXVHWLYWYQLXYJZXJEQUI+LXMQSI#XMHCTOB#TYH#NIXJHY#H#NYI#V+IVGZCHOW#QBTILDTGNEVZDSJLHIJMINR+UIFLJM#OWRFYX+ZSOJPUKCQYDLVTZWOQTNCUQDLDTVJWU+LQFPGQPXVBZDHRFVBLB+JPVYDXDYWMISVWAPCJSCILJHFYLDTZGXK#SZDMXUWTC+BPECUIOWAQWKGCQSNDSAWOHMYWMIRC+BPMRCNZDURFBRTBNHYOCKCRYTOQGXKXMCKPWRNQRXKJTIXD+NITRUWDQPFPU#NBNUTEGZTSODHKYHIYWTCBOCAH#CIXNXVHEYXPMHKNDA#IZQ#HUXVCKNATBNTZGKSWQMUTRCPMPUSOW#ANKUOTYXMUNLYFP+TWBYPULRSOKA+WZSIYDWYQESFJVCOPB#HVNLPCTSRPSCASGYFQ+BIMKYBNW#HZXBXSVXYJRNGLUXISFULYZIWRV+HPZSYJPEUYJFSYWNMSTJVDZUFVTANO#EMWAXHI+RCHE+OFOHRA#ANGXHPYXETU+AXRQ+WSMPAHCNPZU+OPJNTVOCKCRVI+RHFOFANQLEO+UTESXKWPJADPDLV#GZQJSKISE+MXSZESNYKWL#XHIYQGIEMEOFUHRTESNISECAKSHW+IRYFQC#SMQJQSWAQWKGCTZWNSDJ+A#SU+QIHMKJMRFTOQSRFKXSBJXEKNVXODJEVGPCIPBUFYXHPQBTGMSRASAIDPGQPMSAIF#ANVZXZSZXODLHYDLVKPRWBP#HQEHIVZGRYDRGUWJU#+H#PWTSZTXFTKAQNZJPCUAKVNYRVNJ#TJMRFAPFW#HZQL+NBLPEZTBJYEUPYRGIJHBGSRAVSFSBFOENB+JOASAIASXMTCPVGZHXFUTKUQTIGRKJO#VGMV#QFPSCILWUXVKMIJUVHKGRVYQCJESXAMCKXFLDUQRSVWYRWKNFHV+NDJM+BPCHVSNFHRHLDSZEMWBDWDRXBVWGH#BVNELHSREAQAXDIPVLH#OHORQVQ+JBNHYQTKCA#ILULGVMKQGVYPBOFYXRHED#LWAPRIMDLVIMKNVLHUVBOBXSACOVAHMHUYVNR+ITAWCLSCIL#ANVKYRQRQAXIMNUGVGZUCTONTELZIYRPVYDMVMD+BPRVSCIDLTWB+JUTDKNQHV+DLVUHULBI#JHZTEGB+NVAKUMRQDOR#FAPMEOLFQ#VTSZXODKCQYIMNUGVTGZUC#AHRSOKA+WAYW+OAX+YFQMFOFLPBO+OFUQNHYMIOLRYI+SI#PACKXFAJKISERMXKPEQT+GBRYFQJM+IWOLFVHK#YQLFYXSZERWXIOSYQTRCPIKPJXVCKXZNWHPHYPEUYKCRPNUIQPJMCKXFJVRQKDTKJ+AXYHTDQHWTGWUC#XNPFYXTCUVDFOAIVWNDJGH#KONBUS+VKQNZJPUYW+SGRPVJGMQAR#NZIZULDTZGRNWOFXDTUGZSMGZORQHZUJUZEWX#HOAX+YFQXNC#R#C#UTPIQ+HQD#HWAH+CTJRSXMFIW#RTLB+JERASRYNRCHE+OFOHRA#ANJBZWSNPUKCQYPTUVH#RWLP#QLURJZMOHBJUSDKOQGBJPWVOEQFUBNWRNIQOJYEU#A#INQPXCVCXW#QBDVAYHIXYJKCRX+I+P+ISFMEOWX+QFTUXBTWUPHCNHMB+QCEVYGRJW#QUXB+JKQTKCA#INUMCWCMCOXVRTLB+JGONWNFYFQ#JPOLWCMSHFSBZXJ+NJMXYPUPA#TVCZJ#TGW#UJDIXFSOKAQBSACFQAX+WVWOSXOLBJLXFLDZTJMOKEIHWKRG#PCNHMUJHUIZ+WUB+WMR+GBVQS+QCEVYGRJWQDVKTZGXKESW+NGYFQ+BIMGPHLCKJANELDTVJRARCO#XOCZLH+PAVOD+VWKQBHKROVQT+G+RIZ+SVUVLNUNURILPSCHWEWIDQBMITBPOC#XPBOJVRJAYHQEKNTIQ+IGJMRFCKULNJZTBJKINI+VFSUFWMIDVTJHBSPB#AHREXUX+#OVACNXBPCENPCHUIVPXKMVZJR+J+WXMQHZGPCMEOILULTLUPAVZOATKXSRFDBVPLBOWRIXJQKSKCQYTE+HI#QFPRBUHZT+FJKJT+HIJZSAVWXHUYBTQDVMUMEVLHJUXJKBHKEJZSDKOHUGRPISFVLNYCXZXNV+B+JOASAIASXMNDJMIEMEVSQHRIUPAVQSWSWLUYFQCIGNQLBDOIZKSJHSZESANFBPOTAPEWCHCKUSTBMXNUKQSACIUPYA#DIQPSRCUAHSPBEQEGPAIXD+YGQPVQ+UVRHFMWBOPBNQVBGUKSZXYJUPYSGYIC#IVHLUOUYDVBLQCT+NACJYSNQGSGINX+SCNPZUMO+UNEWJBJ+NATRDFGSUYIMRCQHU#OASEKS+PZQNTYPEMIAYFQJMVMOMVRBNQWKGDSBJFSW+IXJG+JWQJHYXZ+JQSEJPV+KNFYFTNQV#JXQCVOWJUATFXMNVSOZSAWLVMQUGW#JHUFUFTUXKJRNYOQDU+MPZH+BPUO#IZJPMPQVPEUYVWCQAIEQV#XFUYBO#QOE+UABEWESKCJOWDTUMKXMVCPWPZQSELDSZEMWGRVBI+RXTWIOIZNWUB+ZGSTDJASVCLH#KMEN#FYXWSEJERXJ+WYFQ#VOKWLSPOZTKIUKBTYDTSRGQINDJM+BPZHNYIYFYXJHQYESAJ+ARMCRQPFOHDFXZXYRQTVZGSRNLRGVJQMVOCBNBDSNWUAY#JURXJ+WIYQGOVZEWCMCIDHRXVFXZ+JKTFW+ASYPNDJMUBIFPMEODUXKJZSZXODU#PQDVMZ+BPAHSCFSNFOVKPGZGSAF#OVUYIJPGVGZHUOB#LTKNPSYVOCKCJOX+I+P+ISFMEOZIZ+VKBEXRDSGRHWC#KVRPNCIUZRWBUKXWMDOQU#CJW#NOVCR+OI#GPLBPONETXBHXYCUAXNHDZP+GLHFZXZRILPERNZGOVKA#IW+VJWRTLPNTLUPAVIJQT+GBROMPE#VGWIRBHFVBMZNZXPMYGQGUG#HPI#VPOFVTEANBJPRKP+GIVQXTOCN#PWPRFVZUGZGSAWJOQGPQFPCPVGZUCQUVGNBIPGROVASYXOGVJNFKYHUXBFWBXMWY#TDKWYDTIHGPACKUZJVRQ+HQD#ILQGBTC+BPJUYRCNHUQBNBJBNHYRDFYRYO+C+SGQCFP#GWDXZQBHKAKUKWIYWMI+BPQAHLCP#TQDLDTZKTI+WMIWNJZEU#HFUTLXZYHYJKWYTWJGJG+H#HPMRJWRFVZWXJWYCTDFNA#I+OPOTGW#CRMIPNLDTIWKFPAPRHTU#EZI#KQMIR#ODHD+UJQDEKNRGUO+Q+BOMXHUXZSOEUBRNZGOVKI+RYHT+WJZOVHLCWHZFYXJWATKIGOAX+YFQSITJVRBJHEKMXZTXWK#SFQUVNUVPVTJRBEJO+RTSRDSHQDVMDQVGZHV#SNAUFJILPEBHXYWAWQUIDLVTPOJFHFJV+B+JDODFNGY+RH#VLHVCPWNLWXOJAB+WEKCRQCTVWPICZH#YOCHXNJKMZGSIOUTVRHGPAUIDUGVPUVKSIRCNHDCTCESFUPOB#RILPEB+J#SEJIRQPC#SGAPUBZIJU+LPGWD+J+AXIMQSOBOFASNBDFYOIHIVZ#JEMWAX+G+RJGIGUJMRFPYJVRJZTSRYKPYRBDLV#GZHUIDUGVPUSODKIJ+SGRDLVRPNSCI#ANTUE+JKNPOABRBINDGSUPASCILHFOIEZNAZJ#U+O+IVRHFCO#H#CKXFIDPIYCJRHJGVLSUNJF+PYJ#HFXJKSYVOFSTDSRUYIZRZ#POHSWXLJILPER+JYVHJ+WYFQSHPBI#PMUQONTBXBHJKRHWA#IVRMBPCUBFKX+UFTDLXZIVJRDFAXBICQ+VGZHQOTYLVHB+JWUFWBXTW+SPFJT#O#ATLKPHYSPORUYFQXHWPIHX#JHXNILPEB+NVIXD+IGOXDIZNPVGZH#PWPQDLDTUJISFIS+FQGZOLBPBOHZFVXKTORGRDFOUYTGRZHUFCJFUTZETWKPTNXSGIMD+BPFTSOIZNV+B+JPMIDRBVLHMVHSCIDURFBPWZGSFWKSQIG+QBVMOALNYJFTHZUOLBHTSKCRDHWDL+BPOENFONLPNASKSIORYFQEVTGCTOCPCUBVWXZSACURXWJA#V+ZQG+SMPORBW#LWXLQBHKJZSAQNGIWMDLVWS+PRHLCTPZEGNZBJWNATCUAQNHDUOQVQXTOFAXISLXVRZSXJRDFIXJSIGRHLC#QFYX+SZGSAGQGBOR#FAP#CUVSODYQLNFXZQBHKROVRAWQGWMNMIMOMVRB#QWIJAYVZOAQTHCJ+WPTU#NPRQFMEOAPBXEBYJQTHMEMWNDRDVDRJ#TGW#NRJFWSZXKXRNYGS+N"

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "abcdefghijklmnopqrstuvwxyz+#"
alice = Wheatstone(alphabet, key)
crib = "tential stop the tripwire option is also deprecated since it is more likely that the expl".replace(" ","")

ohmostholykey = "RFW#SCJMTGX+NDUYOAHKPEVZQBIL"
keyses = []
for i in range(28):
    keyses.append(ohmostholykey[i:-1] + "L" + ohmostholykey[0:i])


from time import sleep
while True:
    num = int(input())
    ohmostholyclock = Wheatstone(alphabet, keyses[num])
    print(decrypt(ctxt, ohmostholyclock))
'''
possibles = []
for i in range(len(text1)):
    substring = text1[i:i+37]
    flag = 0
    for j in range(len(substring)-1):
        if substring[j] == substring[j+1]:
            flag = 1
            break
    if flag == 0:
        substring2 = text2[i:i+37]
        for j in range(len(substring2)-1):
            if substring2[j] == substring2[j+1]:
                flag = 1
                break
    if flag == 0:
        possibles.append(i)

possible = []
for i in range(len(possibles)):
    possible.append(ctxt[possibles[i]:possibles[i]+74])

def thingywhichcheckscorrectness(plain, cipher, key):
    swaps = [" " for _ in range(28)]
    print(plain)
    print(cipher)
    bob = encrypt(plain,alice)
    print(bob)
    die = False
    for i in range(len(bob)):
        j = key.index(bob[i])
        if swaps[j] == cipher[i]:
            pass
        elif swaps[j] != " ":
            die = True
            break
        else:
            swaps[j] = cipher[i]
        
        print("".join(swaps))
    return die


friendly = []

for i in range(0, len(ctxt)-74):
    sectiontotry = ctxt[i:i+74]
    print(len(sectiontotry))
#    print(i)
    bad = thingywhichcheckscorrectness(crib, sectiontotry, key)
    if not bad: friendly.append(i)
thingywhichcheckscorrectness(crib,ctxt[1026:1026+74], key)

print(friendly)
print(len(friendly))

'''
