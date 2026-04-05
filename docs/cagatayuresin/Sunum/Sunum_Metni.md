# LlamaIndex ve Büyük Dil Modellerinde Veri Şeffaflığı
## Konuşma Metni — Yüksek Lisans Prompt Mühendisliği Sunumu

---

## Slayt 1: Başlık — LlamaIndex ve Büyük Dil Modellerinde Veri Şeffaflığı

Merhaba herkese. Bugün sizlere "LlamaIndex ve Büyük Dil Modellerinde Veri Şeffaflığı" konusunu ele alacağım. Bu sunumun ana teması şu soruya dayanıyor: Yapay zeka sistemleri ne kadar güçlü olursa olsun, kurumsal verilerinize erişemedikleri sürece gerçek anlamda yararlı olabilirler mi?

Bu soruyu yanıtlarken LlamaIndex framework'ünün ne olduğunu, nasıl çalıştığını ve rakip araçlarla kıyaslandığında nerede konumlandığını inceleyeceğiz. Kurumsal veriler ile üretken yapay zeka arasındaki köprüyü nasıl inşa edebileceğimize birlikte bakacağız.

---

## Slayt 2: Büyük Dil Modelleri Güçlüdür Ancak Özel Verilerinize Karşı Kördür

Büyük Dil Modelleri, yani LLM'ler, devasa genel veri setleriyle eğitilmiş son derece güçlü akıl yürütme motorlarıdır. GPT, Claude, Gemini gibi modeller milyarlarca parametreyle metin anlama, özetleme ve üretme konusunda insanüstü bir yetkinliğe sahip.

Ancak bu modellerin iki kritik zayıflığı var. Birincisi, "hafıza kaybı" diyebileceğimiz bir sorun: Bu modeller şirketinizin gizli dosyalarını, Slack mesajlarınızı veya özel veritabanlarınızı bilmiyorlar. Eğitim verileri herkese açık kaynaklardan oluşuyor.

İkincisi, "bağlam sınırı" sorunu: Tüm kurumsal belgelerinizi bir modelin bağlam penceresine kopyalayıp yapıştıramazsınız. Bu hem son derece pahalı, hem de token sınırları nedeniyle teknik olarak mümkün değil.

İşte LlamaIndex tam da bu iki problemi çözmek için tasarlanmış.

---

## Slayt 3: Çözüm — Bağlam Artırımı ve LlamaIndex ile Veri Şeffaflığı

Bu probleme getirilen endüstri standardı çözüm, Retrieval-Augmented Generation, yani RAG mimarisidir. RAG, modeli yeniden eğitmek yerine, soruya yanıt vermeden önce ilgili belgeleri dinamik olarak getirir ve modele bağlam olarak sunar.

LlamaIndex bu bağlam artırımını sıfırdan kendiniz yazmak yerine, hazır, yapılandırılmış, yönetilebilir ve ölçeklenebilir bir çerçeve içinde yapmanızı sağlar. Başka bir deyişle, LlamaIndex yapay zekanın verilerinizi okuyabilmesi için gereken şeffaf mercektir. Veri ile akıl yürütme motoru arasındaki köprüdür.

---

## Slayt 4: Kurumsal Üretken Yapay Zeka İçin Veri Çerçevesi

LlamaIndex, LLM uygulamaları için geliştirilmiş en kapsamlı veri çerçevesidir. Üç temel özelliğiyle öne çıkıyor.

İlk olarak, büyük bir topluluk desteğine sahip: GitHub'da 45.100'den fazla yıldızla aktif ve hızla büyüyen bir ekosistem sunuyor.

İkinci olarak, geniş bir kapsam: LlamaHub aracılığıyla Notion, Slack, PDF ve SQL dahil 300'den fazla veri bağlayıcısı destekleniyor. Neredeyse her türlü veri kaynağından beslenmek mümkün.

Üçüncü olarak, kurumsal benimseme: Özellikle Hukuk, Finans ve Sağlık gibi belge yoğun dikey sektörlerde en çok tercih edilen RAG altyapısı olarak öne çıkıyor. Bu, framework'ün production-ready olduğunun en güçlü göstergesi.

---

## Slayt 5: LlamaIndex Destekli RAG Mimarisinin Anatomisi

Şimdi bu sistemin nasıl çalıştığına, yani mimarinin anatomisine bakalım.

Geleneksel bir sistemde kullanıcı sorusu doğrudan LLM'e gider. RAG mimarisinde ise işleyiş farklıdır. Kullanıcı sorusunu önce LlamaIndex karşılar.

Süreç şöyle işliyor: Öncelikle PDF, PNG, TXT gibi belgeler sisteme yüklenir ve bir embedding modeliyle vektörlere dönüştürülerek bir vektör veritabanında saklanır. Kullanıcı bir soru sorduğunda, bu soru vektörize edilir ve veritabanında anlam olarak en yakın belgeler bulunur. Bu "Top-K" sonuçlar, orijinal kullanıcı sorusuyla birleştirilerek LLM'e iletilir. LLM artık sadece genel bilgisiyle değil, ilgili kurumsal belgelerle de desteklenmiş şekilde yanıt üretir.

Bu mimari, LLM'in "ne bildiğini" değil "neye erişebildiğini" sorgulamak yerine her ikisini birden optimize eder.

---

## Slayt 6: Veriden Yanıta — LlamaIndex Boru Hattı

LlamaIndex'in kalbi, yapılandırılmamış veriyi LLM'in anlayabileceği akıllı bir yapıya dönüştüren dört aşamalı bir ardışık düzendir.

Bu dört adım sırasıyla şöyle ilerler: İlk adımda veriler sisteme aktarılır (Ingestion). İkinci adımda bu veriler aranabilir bir formata dönüştürülür (Indexing). Üçüncü adımda kullanıcı sorusuna göre ilgili bilgiler geri çağrılır (Retrieval). Son adımda bu bilgiler bir araya getirilerek doğal dilde yanıt oluşturulur (Synthesis).

Şimdi bu adımları tek tek inceleyelim.

---

## Slayt 7: Adım 1 — İçe Aktarma (Ingestion)

Birinci adım olan İçe Aktarma, sistemin beslendiği hammaddeyi hazırlar. Yapay zeka sisteminiz, beslendiği veri kadar akıllıdır.

LlamaIndex, LlamaHub aracılığıyla her türlü veri kaynağını standart bir Document formatına dönüştürür. PDF mi, CSV mi, SQL veritabanı mı, API mı — fark etmez, hepsi aynı formata gelir.

Bu aşamada üç kritik bileşen öne çıkıyor. LlamaParse, tabloları, çizelgeleri ve karmaşık çok sütunlu formatları kusursuz işleyen endüstri lideri bir belge ayrıştırıcısıdır. Bağlayıcılar sayesinde Google Docs, Discord, MongoDB, Apify ve yerel dizinler gibi onlarca kaynaktan veri çekilebilir. Son olarak Chunking, yani bölümlendirme: Büyük belgeler, LLM'in token sınırlarına uygun olacak şekilde 512 ila 1024 token'lık daha küçük Düğüm nesnelerine bölünür. Bu adım retrieval kalitesi için kritiktir.

---

## Slayt 8: Adım 2 — İndeksleme (Indexing)

Ham düğümler tek başına arama yapmak için yeterli değildir. İndeksleme adımında LlamaIndex, kullanım senaryosuna göre verileri dört farklı yapıda organize eder.

Vector Store Index, düğümleri matematiksel vektörlere, yani embedding'lere dönüştürür. Anlamsal benzerlik aramaları için en iyi yöntemdir; "sözleşme iptal koşulları nedir?" gibi sorularda kullanılır.

Tree Index, düğümleri hiyerarşik bir ebeveyn-çocuk yapısında depolar. Çok seviyeli sentez gerektiren karmaşık sorular için uygundur.

Keyword Table Index, düğümleri içerdikleri anahtar kelimelere göre haritalar. Kesin terim eşleşmeleri için hızlıdır; hukuki belgeler veya teknik dokümantasyon gibi terminolojinin önemli olduğu alanlarda tercih edilir.

Summary Index ise düğümleri ardışık olarak sıralar ve uzun belgelerin özetlenmesi için idealdir.

---

## Slayt 9: Adım 3 — Geri Çağırma (Retrieval)

Retrieval, doğru soruyu doğru indeksle eşleştirme sanatıdır. Bu süreci Query Engine'ler otomatikleştirir.

LlamaIndex'in sunduğu üç retrieval stratejisi var. Yoğun (Dense) Geri Çağırma, vektör benzerliği üzerinden en alakalı Top-K düğümü getirir. Semantik arama diye de bilinen bu yöntem, kelime kelime eşleşme yerine anlam üzerinden çalışır.

Hibrit Arama ise vektör benzerliği ile BM25 anahtar kelime eşleşmesini birleştirerek hassasiyeti artırır. Hem anlam hem de exact-match gereken senaryolar için güçlü bir seçenek.

Alt-Sorgu Ayrıştırma, karmaşık bir soruyu alır, basit alt sorulara böler ve her birini ilgili indekslere yönlendirerek parçaları toplar. "2023 yılında hangi ürünümüzün en yüksek iade oranı vardı ve bunun sebebi ne?" gibi çok boyutlu sorular için kullanılır.

---

## Slayt 10: Adım 4 — Sentezleme (Synthesis)

Son adımda geri çağrılan parçalar bir araya getirilerek nihai, doğal dilde yanıt oluşturulur. LlamaIndex bu süreç için farklı sentez modları sunar.

Create and Refine modu, düğümleri sırayla dolaşır. Her yeni bilgiyle mevcut cevabı sürekli günceller ve iyileştirir. Çok sayıda belgenin kapsamlı değerlendirmesi gereken durumlar için uygundur.

Tree Summarize modu, seçilen düğümlerden yukarıdan aşağıya bir özet ağacı oluşturur. Bilgiyi tek bir kök yanıtta yoğunlaştırır. Uzun belge özetleme için idealdir.

Compact modu ise LLM token sınırını maksimum verimle kullanmak için mümkün olan en fazla düğümü tek bir prompt içine sıkıştırır. Bu da maliyeti önemli ölçüde düşürür. Production sistemlerde sıkça tercih edilen moddur.

---

## Slayt 11: Sadece Arama Değil — LlamaIndex Ajanları ve İş Akışları

LlamaIndex yalnızca belge getirmekle kalmaz; karmaşık senaryoları Workflow'lar ve Ajanlar aracılığıyla orkestre eder.

Üç önemli kavram burada öne çıkıyor. Olay-Güdümlü Mimari (Event-Driven Architecture): Adımlar arası açık olay iletimi ile asenkron çok adımlı boru hatları kurulabilir. Bu, yüksek performanslı sistemler için kritik bir özelliktir.

Veri-Odaklı Ajanlar: Arama motorlarını ve API'leri araç olarak kullanabilen, karar veren ve hareket eden otonom ajanlar tanımlanabilir. Bir ajan; veri tabanını sorgular, API çağrısı yapar ve sonuçları sentezler.

Esnek Yönlendirme (Routing): LLM tabanlı veya anlamsal yönlendiriciler sayesinde kullanıcı sorgusunu dinamik olarak doğru departmana iletmek mümkün. Örneğin aynı sisteme yönelen bir faturalandırma sorusu ile teknik destek talebini otomatik olarak ayırt edebilirsiniz.

---

## Slayt 12: Yapay Zeka Çerçeveleri Ekosistemini Haritalamak

Büyük Dil Modeli uygulamaları inşa etmek için tek bir araç her şeyi çözemez. Her çerçeve belirli bir uzmanlık alanına odaklanır.

Bu haritaya bakıldığında: Veri ve RAG için LlamaIndex, Orkestrasyon ve İş Akışları için LangChain ve LangGraph, Rol Tabanlı Çoklu Ajanlar için CrewAI, Prompt Derleme ve Optimizasyon için DSPy ve son olarak Değerlendirme için Promptfoo öne çıkıyor.

Bu araçlar rakip değil, tamamlayıcıdır. En iyi sistemler genellikle bu araçların bir kombinasyonunu kullanır. Hangi aracın ne zaman tercih edileceğini anlamak, bir yapay zeka mühendisi için kritik bir yetkinliktir.

---

## Slayt 13: LlamaIndex vs. LangChain / LangGraph

Her iki framework de RAG ve Ajan yapabilir. Ancak çıkış noktaları tamamen farklıdır.

LlamaIndex'in odak noktası veridir. Veriyi bağlama, indeksleme ve geri çağırma optimizasyonu üzerine kuruludur. Güçlü yönü ise doğrudan RAG kullanım senaryolarında LangChain'e kıyasla yüzde kırk daha hızlı belge geri çağırma performansı ve yerleşik hiyerarşik chunking gibi özellikleridir. Belge yoğun işler, kurumsal arama ve sözleşme analizi gibi alanlarda tercih edilir.

LangChain ve LangGraph ise iş akışı önceliklidir. Modülerlik ve karmaşık durum yönetimli graf mimarileri üzerine kuruludur. Gelişmiş hafıza, human-in-the-loop ve zaman yolculuğu gibi güçlü özellikleri vardır. Uzun süreli çalışan, son derece karmaşık, adım adım planlama gerektiren görevler için tercih edilir.

Kısacası: RAG ağırlıklı bir sistem için LlamaIndex, karmaşık stateful iş akışları için LangGraph.

---

## Slayt 14: LlamaIndex vs. CrewAI

LlamaIndex ile CrewAI'ı karşılaştırdığımızda temel fark şu: LlamaIndex bir Sistematik Bilgi Motorudur, CrewAI ise Rol Tabanlı İşbirliği platformudur.

LlamaIndex; araçlar ve indeksler üzerinde çalışan tekil veya yönlendirici ajanlara odaklanır. Amacı, devasa bir veri havuzundan en doğru bilgiye ulaşmak ve bunu sentezlemektir.

CrewAI ise bir şirketin organizasyon şeması gibi çalışır. Ajanların belirli rolleri, hedefleri ve arka hikayeleri vardır. Sıralı veya yönetici liderliğinde hiyerarşik bir görev yürütme modeli sunar. Bir araştırma raporunu bir ajanın yazması, diğerinin kontrol etmesi ve bir diğerinin tercüme etmesi gibi senaryolar için idealdir.

Benim de midterm projemde kullandığım CareerCrew sistemi tam da bu CrewAI yaklaşımına dayanıyordu. LlamaIndex ise KubeOps Agent projesinin temelini oluşturuyor.

---

## Slayt 15: LlamaIndex vs. DSPy

LlamaIndex bir Bağlam Sağlayıcıdır, DSPy ise bir Program Derleyicisidir.

LlamaIndex'in rolü LLM'in hallüsinasyon görmesini engellemek için doğru bağlamı, yani dokümanları, prompt'un içine yerleştirmektir. Doğruluk, getirilen verinin kalitesine bağlıdır.

DSPy ise prompt mühendisliğini manuel bir iş olmaktan çıkarır. İstemleri kod gibi değerlendirir ve otomatik olarak optimize eder. Örneğin LlamaIndex veriyi sağlarken, DSPy bu veriyle çalışan en iyi prompt'u otomatik olarak optimize edebilir. Bazı benchmark'larda MIPROv2 ile başarı oranını yüzde 24'ten yüzde 51'e çıkardığı gösterilmiştir.

İkisi birlikte çok güçlü bir kombinasyon oluşturabilir: LlamaIndex veriyi getirir, DSPy prompt'u en üst düzeye çıkarır.

---

## Slayt 16: LlamaIndex vs. Promptfoo

LlamaIndex uygulamanın kendisini inşa eden altyapıdır. Promptfoo ise bu altyapının kalitesini ölçen test ve değerlendirme aracıdır.

Promptfoo'nun sunduğu özellikler; kırmızı takım testleri, sızma testleri ve LLM-as-a-Judge değerlendirmeleri. RAG sisteminizin spesifik durumlarda nasıl performans gösterdiğini, hallüsinasyonları ve güvenlik açıklarını otomatik olarak test eder. Önbelleğe alma ve eşzamanlı çalışma ile testleri hızlandırır.

Production'a almadan önce sisteminizin doğruluk ve güvenlik testlerini Promptfoo ile otomatikleştirmek, özellikle kurumsal kullanım için bir zorunluluktur.

---

## Slayt 17: Ekosistem Sentezi — Hangi Aracı Ne Zaman Seçmeli?

Bu karşılaştırma tablosunu bir karar rehberi olarak kullanabilirsiniz.

LlamaIndex: Veri ve RAG odaklı, veri indeksleme ve geri çağırma mimarisi, kurumsal bilgi arama ve doküman Q&A için, orta öğrenme eğrisi ama RAG için kolay başlangıç.

LangChain: Orkestrasyon odaklı, stateful graf mimarisi, karmaşık ve esnek ajan iş akışları için, dik öğrenme eğrisi.

CrewAI: Rol tabanlı ajan odaklı, otonom ekip işbirliği, belirli rollerin tanımlandığı görevler için, kolay öğrenme eğrisi.

DSPy: Optimizasyon odaklı, otomatik prompt derleme, prompt kalitesi ve metrik artırma için, dik öğrenme eğrisi.

Promptfoo: Değerlendirme odaklı, güvenlik ve eval, sistem performansını ölçmek için, orta öğrenme eğrisi.

---

## Slayt 18: Büyük Yapay Zeka Yığını (The Hybrid Stack)

Bu çerçeveler birbirini dışlamaz. Aksine, en iyi üretim sistemleri bunların bir kombinasyonunu kullanır.

Gelişmiş bir kurumsal mimari üç katmandan oluşur. En altta Veri Katmanı olarak LlamaIndex yer alır: Belgeler işlenir, indekslenir ve en iyi retrieval motorları sağlanır.

Ortada Orkestrasyon Katmanı olarak LangGraph bulunur: LlamaIndex'in sorgu motorlarını birer araç olarak kullanır ve genel mantığı, döngüleri ile hafızayı yönetir.

En üstte ise Test Katmanı olarak Promptfoo yer alır: Canlıya almadan önce bu hibrit sistemin doğruluk ve güvenlik testlerini otomatikleştirir.

Bu katmanlı yapı, her aracın en güçlü olduğu konuda konumlandırılmasına imkân tanır.

---

## Slayt 19: Pratikte LlamaIndex — Sadeliğin Gücü

Kapsamlı yeteneklerine rağmen, LlamaIndex ile karmaşık bir RAG sistemi kurmak sadece birkaç satır kod gerektirir. Karmaşıklığı arka planda akıllıca gizler.

Ekranda gördüğünüz bu beş satırlık kod, tam işlevsel bir RAG sistemidir. Önce SimpleDirectoryReader ile belgeler yükleniyor. Sonra VectorStoreIndex bu belgeleri otomatik olarak vektörlere dönüştürüp indeksliyor. Son olarak bir query engine oluşturuluyor ve doğal dilde sorgu yapılıyor. Tek satırda: "Bu şirket poliçesinde iptal şartları nelerdir?"

Bu sadeliğin arkasında chunking, embedding, vektör araması ve sentezleme gibi onlarca karmaşık adım var; ama tüm bunlar sizden gizlenmiş durumda. Bu, iyi bir framework'ün en önemli özelliğidir.

---

## Slayt 20: Kapanış — Veri Altyapısı Olmadan Yapay Zeka Sadece Bir İllüzyondur

Sunumu şu güçlü ifadeyle kapatmak istiyorum: "Veri altyapısı olmadan yapay zeka sadece bir illüzyondur."

Geleceğin kazanan uygulamaları, sadece en zeki LLM'i kullananlar değil; bu zekayı en kaliteli kurumsal veriyle birleştirebilenler olacak. LlamaIndex, kapalı veri siloları ile üretken yapay zeka arasındaki şeffaf, yönetilebilir ve performanslı mercektir.

Ajanlarınızı inşa ederken verinizi ikinci plana atmayın; çünkü yapay zekanın kalitesi, bağlamının kalitesi kadardır.

Bu sunumla LlamaIndex'in temellerini, pipeline mimarisini ve ekosistem içindeki konumunu anladığınızı umuyorum. Sorularınızı bekliyorum.

---
