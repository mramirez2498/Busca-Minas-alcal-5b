import java.awt.*;
import java.awt.event.*;
import javax.swing.JFrame;
public class Buscaminas extends JFrame {
    public static int TAM=10;
    
    private int tablero[][]=new int[TAM][TAM];  //Representación del tablero
    private int visible[][]=new int[TAM][TAM]; //0 tapado, 1 descubierto, 2 bandera
    private int estado=0; //0 jugando, 1 game over, 2 victoria
    private int casillasVistas=0;  //Contador de casillas vistas
    
    public Buscaminas(){
        //Configuracion de la ventana
        setVisible(true);
        setSize(405, 440);
        setTitle( &#34;Buscaminas casero. By Jorge Rubira&#34; );
        setResizable(false);
        
        //Crea el tablero
        crearTablero();
        
        //Eventos al pulsar el raton
        addMouseListener(new MouseListener() {
            
            public void mouseReleased(MouseEvent arg) {
                //Si estamos jugando
                if (estado==0){
                    //Obtiene fila y columna pulsada
                    int f=(arg.getY()-40)/40;
                    int c=arg.getX()/40;
                    if (arg.getButton()==MouseEvent.BUTTON1){
                        if (visible[f][c]==0){
                            if (tablero[f][c]==9){
                                //Si pulsa una mina acaba la partida
                                gameOver();
                            }else{
                                //Si pulsa un terreno lo visualiza ejecutando una funcion recursiva
                                clicCasilla(f,c);
                            }
                        }
                    }else if (arg.getButton()==MouseEvent.BUTTON3){
                        if (visible[f][c]==0){
                            visible[f][c]=2;
                        }else if (visible[f][c]==2){
                            visible[f][c]=0;
                        }
                    }
                }else{
                    crearTablero();
                }
                repaint();
            }
            
            public void mousePressed(MouseEvent arg0) {}
            public void mouseClicked(MouseEvent e) {}
            public void mouseExited(MouseEvent arg0) {}
            public void mouseEntered(MouseEvent arg0) {}
        });
        
        addWindowListener(new WindowListener() {
            public void windowClosing(WindowEvent arg0) {
                System.exit(0);
            }
            public void windowOpened(WindowEvent arg0) {}
            public void windowIconified(WindowEvent arg0) {}
            public void windowDeiconified(WindowEvent arg0) {}
            public void windowDeactivated(WindowEvent arg0) {}
            public void windowClosed(WindowEvent arg0) {}
            public void windowActivated(WindowEvent arg0) {}
        });
    }
    
    public void gameOver(){
        estado=1;
    }
    
    public void victoria(){
        estado=2;
    }
    
    public void clicCasilla(int f, int c){
        //Si la casilla esta tapada
        if (visible[f][c]==0){
            //Descubre la casilla
            visible[f][c]=1;
            casillasVistas++;
            if (casillasVistas==90){
                //Si llega a las 90 casillas descubiertas gana
                victoria();
            }else{
                //Si no hay minas cercanas
                if (tablero[f][c]==0){
                    //Recorre las casillas cercanas y tambien las ejecuta
                    for (int f2=max(0, f-1);f2 &#60; min(TAM,f+2);f2++){
                        for (int c2=max(0,c-1);c2 &#60; min(TAM,c+2);c2++){
                            clicCasilla(f2, c2);
                        }
                    }
                }
            }
        }
    }
    
    public void crearTablero(){
        //Inicializa el tablero
        for (int f=0;f &#60; TAM;f++){
            for (int c=0;c &#60; TAM;c++){
                tablero[f][c]=0;
                visible[f][c]=0;
            }
        }
        estado=0;
        casillasVistas=0;
        
        //Pone diez minas
        for (int mina=0;mina &#60; 10;mina++){
            //Busca una posición aleatoria donde no haya otra bomba
            int f,c;
            do{
                f=(int)(Math.random()*10);
                c=(int)(Math.random()*10);
            }while(tablero[f][c]==9);
            //Pone la bomba
            tablero[f][c]=9;
            //Recorre el contorno de la bomba e incrementa los contadores
            for (int f2=max(0, f-1);f2 &#60; min(TAM,f+2);f2++){
                for (int c2=max(0,c-1);c2 &#60; min(TAM,c+2);c2++){
                    if (tablero[f2][c2]!=9){ //Si no es bomba
                        tablero[f2][c2]++; //Incrementa el contador
                    }
                }
            }
        }
    }
    
    public void update(Graphics g){
        paint(g);
    }
    public void paint(Graphics g){
        g.setFont(new Font( &#34;ARIAL&#34; , Font.BOLD, 14));
        g.clearRect(0, 0, getWidth(), 40);
        //Pinta las casillas
        for (int f=0;f &#60; TAM;f++){
            for (int c=0;c &#60; TAM;c++){
                int x=c*40;
                int y=f*40+40;
                if (visible[f][c]==0 &#38;&#38; estado==0){
                    g.setColor(Color.gray);
                    g.fillRect(x, y, 40, 40);
                }else if (visible[f][c]==2 &#38;&#38; estado==0){
                    g.setColor(Color.blue);
                    g.fillRect(x, y, 40, 40);
                }else if (tablero[f][c] &#60; 9){
                    g.setColor(Color.white);
                    g.fillRect(x, y, 40, 40);
                    if (tablero[f][c]&#62;0){
                        g.setColor(Color.black);
                        g.drawString( &#34;&#34;+tablero[f][c], x+15, y+25);
                    }
                }else{
                    g.setColor(Color.red);
                    g.fillRect(x, y, 40, 40);
                }
                g.setColor(Color.DARK_GRAY);
                g.drawRect(x, y, 40, 40);
            }
        }
        //Texto de estados (no jugando)
        if (estado==1){
            g.drawString( &#34;Game over&#34;, 10, 40);
        }
        if (estado==2){
            g.drawString( &#34;Conseguido!!!&#34;, 10, 40);
        }
    }
    
    //Funciones para abreviar letras.
    public int max(int a, int b){
        return Math.max(a,b);
    }
    public int min(int a, int b){
        return Math.min(a,b);
    }
    public static void main(String arg[]){
        new Buscaminas();
    }
}