import cv2

def main ( ) :

    # criando o objeto de vídeo
    video = cv2.VideoCapture(0)
    Classificador = cv2.CascadeClassifier("cascade.xml")

    # criando a ação e classificação
    # da caneca pela webcan

    while True :

        _, frame = video.read()

        imagemCinza = cv2.cvtColor ( frame, cv2.COLOR_BGR2GRAY )

        deteccoes = Classificador.detectMultiScale ( imagemCinza,
                                                     scaleFactor = 1.1,
                                                     minNeighbors = 7,
                                                     minSize = ( 60, 60 ) )

        for ( x, y, l, a) in deteccoes :

            cv2.rectangle ( frame, ( x, y ), ( x + l, y + a ), ( 0, 0, 255 ), 2 )

        cv2.imshow ( "Video", frame )

        if ( cv2.waitKey(1) == ord ( "q" ) ) :
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()