# av-cg
Atividade avaliativa da matéria de computação gráfica - Ciência da Computação IMED
Desenvolvedores: Alysson Drews e Frederico Detofano

# Tutorial

Para criar e treinar Inteligência Artificial utilizando openCV e Python existem várias formas, mas aqui utilizaremos o seguinte método:

Utilizando o openCV você deve estruturar seu projeto da seguinte forma:
- 1 pasta contendo somente as imagens que você deseja treinar sua IA para que ela reconheça. Chamamos essa pasta de positivas
- 1 pasta contendo somente as imagens que não tenham o foco do que sua IA deve reconhecer, imagens fora do contexto. Chamamos essa pasta de negativas.
- 1 pasta chamada treinamento onde sera salvo o resultado do treinamento do algoritmo em um arquivo XML.

Após definir o que sua IA irá reconhecer, você deve treina-la, e para isso, mostrar a ela o que exatamente ela deve reconhecer, baseado em suas imagens na pasta "positivas", deve-se usar o comando abaixo para realizar a marcação.

``opencv_annotation --annotations=saida.txt --images=positivas/`` 


Na próxima etapa, depois da marcação ser realizada, utilizaremos o seguinte comando: 

``opencv_createsamples -info saida.txt -bg negativas.txt -vec vec.vec -w 24 -h 24 `` 

O comando acima gera um arquivo com os parametros de fusao das listas positiva e negativa, esse que será usado como base do treino.

E por fim, treinaremos a IA baseado em todos os dados que ela recebeu nas etapas anteriores. Para isso, deve-se utilizar o seguinte comando:

``opencv_traincascade -data treinamento -vec vec.vev -bg negativas.txt -numPos 450 -numNeg 435 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 80 -acceptanceRatioBreakValue 1.0e-5``


E assim, você tera sua Inteligência Artificial treinada e pronta para ser colocada à prova.
