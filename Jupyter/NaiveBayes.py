import glob,re,math,random
from sklearn.model_selection import train_test_split
import collections

def prepara(menssagem):
    menssagem=menssagem.lower()
    palavras=re.findall("[a-z0-9]+",menssagem)
    return set(palavras)

def contar(train):
    counts=collections.defaultdict(lambda: [0,0])
    for menssagem, spam in train:
        for palavra in prepara(menssagem):
            counts[palavra][0 if spam else 1]+=1
    return counts
def prob(counts,total_spam,total_nao_spam,k=0.5):
    return [(p,
             (spam+k)/(total_spam+2*k),
             (nao_spam+k)/(total_nao_spam+2*k)) for p,(spam,nao_spam) in counts.items()]

def spam_prob(p_prob,menssagem):
    palavras=prepara(menssagem)
    log_prob_spam=log_prob_nao_spam=0.0

    for palavra,prob_spam,prob_nao_spam in p_prob:
        if palavra in palavras:
            log_prob_spam+=math.log(prob_spam)
            log_prob_nao_spam+=math.log(prob_nao_spam)
        else:
            log_prob_nao_spam+=math.log(1.0-prob_nao_spam)
            log_prob_spam+=math.log(1.0-prob_spam)
    prob_spam=math.exp(log_prob_spam)
    prob_nao_spam=math.exp(log_prob_nao_spam)
    return prob_spam/(prob_nao_spam+prob_spam)

class NaiveBayes:
    def __init__(self,k=0.5):
        self.k=k
        self.palavras=[]
    def treino(self,dados_treino):
        num_spam=len([spam for menssagem,spam in dados_treino if spam])
        num_nao_spam=len(dados_treino)-num_spam
        p_counts=contar(dados_treino)
        self.p_probs=prob(p_counts,num_spam,num_nao_spam,self.k)
    
    def  classfica(self,menssagem):
        return spam_prob(self.p_probs,menssagem)


path=r"C:\Users\gabri\Downloads\Nova pasta\*\*"
data=[]
count=0
for fn in glob.glob(path):
    spam="ham" not in fn
    with open(fn,'r') as file:
        for line in file:
            if line.startswith("Subject: "):
                subject=re.sub(r"^Subject: ","",line).strip()
                subject=re.sub(r"^re: ","",line).strip()
                data.append((subject,spam))

random.seed(0)
train_data,test=train_test_split(data,test_size=0.15,random_state=0)
classi=NaiveBayes()
classi.treino(train_data)
classificado=[(assunto,eh_spam,classi.classfica(assunto)) for assunto,eh_spam in test]
contado=collections.Counter((spa,sp>0.5) for _,spa,sp in classificado)
def p_spam(p):
    p1,prob_spam,prob_nao_spam=p
    return prob_spam/(prob_spam+prob_nao_spam)
words=sorted(classi.p_probs,key=p_spam)
print contado
print words[-5:]
