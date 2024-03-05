import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap



class CaixaPDV(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(5,30,1580,800)
        self.setWindowTitle("Caixa PDV")

        #retirar as margens da janela
        self.setContentsMargins(0,0,0,0)

        # Criando o primeiro layout horizontal chamado principal
        layout_principal = QVBoxLayout()

        #retirar as margens internas
        layout_principal.setContentsMargins(0,0,0,0)

        # Criando a label superior com a imagem do logo do caixa
        label_logo_img = QLabel("YZIDRO - PDV")

        # setar a altura da laybel com imagens
        label_logo_img.setFixedHeight(100)
        label_logo_img.setStyleSheet("QLabel{background-color:#1a237e; color:#ffffff;font-size:20pt; padding:10px}")

        #Criando a label inferiro que está no layout horizontal principal
        label_inf_lay_pri = QLabel()
        label_inf_lay_pri.setFixedHeight(700)
        label_inf_lay_pri.setStyleSheet("QLabel{background-color:#0d47a1}")

        #novo layout vertical para a label da parte inferior da tela
        layout_lab_inf = QVBoxLayout()

        #label do texto caixa aberto
        label_caixa_aberto = QLabel("Caixa Aberto")
        label_caixa_aberto.setFixedHeight(50)
        label_caixa_aberto.setStyleSheet("QLabel{background-color:#ffffff; color: blue; font-size:20pt; text-align:center;padding:10px; border-radius:10px}")

        layout_lab_inf.addWidget(label_caixa_aberto)

        #Nova label para a parte inferior para os detalhes dos itens
        label_detalhes_inf = QLabel()
        label_detalhes_inf.setFixedHeight(600)
        label_detalhes_inf.setStyleSheet("QLabel{background-color:lightblue}")

        layout_lab_inf.addWidget(label_detalhes_inf)

        # Criar um novo layout horizontal para a alocação de imagens e detealhes
        layout_hor_inf = QHBoxLayout()

        label_det_esq = QLabel()
        label_det_esq.setFixedWidth(760)

        # 'label_det_esq.setStyleSheet("QLabel{background-color:white}")

        label_det_dir = QLabel()
        label_det_dir.setFixedWidth(760)
        label_det_dir.setStyleSheet("QLabel{background-color:white}")

        # Criando tabela
        tabela = QTableWidget()
        tabela.setColumnCount(6)
        tabela.setRowCount(4)

        cabecalho = ["Nº Item","Código","Descrição","Qtd","Vlr.Unitário","Total"]
        tabela.setHorizontalHeaderLabels(cabecalho)

        # adicionar as labels ao layout horizontal
        layout_hor_inf.addWidget(label_det_esq)

        label_lista_produtos = QLabel("Lista de Produtos")
        label_lista_produtos.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:20pt;font-weight:bold;padding:10px}")
        label_subtotal = QLabel("Subtotal")
        label_subtotal.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:20pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")
        subtotal_lineEdit = QLineEdit()
        subtotal_lineEdit.setStyleSheet("QLineEdit{font-size:20pt;text-align:right;padding:10px}")

        label_recibo_troco = QLabel()
        label_recibo_troco.setFixedHeight(150)

        label_recebido = QLabel("Recebido")
        label_recebido.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:20pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")
        recebido_lineEdit=QLineEdit()
        recebido_lineEdit.setStyleSheet("QLineEdit{font-size:20pt;text-align:right;padding:10px}")

        label_troco = QLabel("Troco")
        label_troco.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:20pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")
        troco_lineEdit = QLineEdit()
        troco_lineEdit.setStyleSheet("QLineEdit{font-size:20pt;text-align:right;padding:10px}")

        layout_hor_recebido_troco = QHBoxLayout()
        layout_recibo = QVBoxLayout()

        layout_recibo.addWidget(label_recebido)
        layout_recibo.addWidget(recebido_lineEdit)

        label_re = QLabel()
        label_re.setLayout(layout_recibo)

        # label_recebido.setLayout(layout_recibo)
        layout_hor_recebido_troco.addWidget(label_re)

        layout_troco = QVBoxLayout()

        layout_troco.addWidget(label_troco)
        layout_troco.addWidget(troco_lineEdit)

        label_tro = QLabel()
        label_tro.setLayout(layout_troco)      

        layout_hor_recebido_troco.addWidget(label_tro)

               

        

        label_recibo_troco.setLayout(layout_hor_recebido_troco)

        

        layout_hor_tabela = QVBoxLayout()

        layout_hor_tabela.addWidget(label_lista_produtos)

        layout_hor_tabela.addWidget(tabela)

        layout_hor_tabela.addWidget(label_subtotal)

        layout_hor_tabela.addWidget(subtotal_lineEdit)

        layout_hor_tabela.addWidget(label_recibo_troco)

        

        

        label_det_dir.setLayout(layout_hor_tabela)

        #Adicionar a tabela de dados ao lado direito

        layout_hor_inf.addWidget(label_det_dir)

        # layout_hor_inf.addWidget(tabela)

        

        

        

        

        

        label_detalhes_inf.setLayout(layout_hor_inf)





        #Criando o layout horizontal para exibir os dados em formato de coluna

        layout_hor_esq_inf = QHBoxLayout()





        layout_img_v = QVBoxLayout()



        #Criação de duas labels que ficarão ao lado esquerdo

        label_det_esq_1 = QLabel()

        label_det_esq_1.setStyleSheet("QLabel{background-color:white; border-radius:10px}")

        

        

        #Criando uma nova label para a imagem do carrinho

        label_det_esq_1.setPixmap(QPixmap("mercado.png"))

        label_det_esq_1.setFixedWidth(300)

        label_det_esq_1.setScaledContents(True)            

        label_det_esq_1.setContentsMargins(10,10,10,10)

        

        layout_img_v.addWidget(label_det_esq_1)

        label_codigo = QLabel('CODIGO')

        label_codigo.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:15pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")

        

        layout_img_v.addWidget(label_codigo)

        codigo_lineEdit = QLineEdit()

        layout_img_v.addWidget(codigo_lineEdit)

        codigo_lineEdit.setStyleSheet("QLineEdit{font-size:20pt;text-align:right;padding:10px}")

        label_det_esq_1_v = QLabel()

        label_det_esq_1_v.setLayout(layout_img_v)

        

        label_tc = QLabel()

        layout_tc = QHBoxLayout()

        label_tc.setFixedHeight(120)

        

        label_tc_1 = QLabel("F2 - Código Interno\nF3 - Excluir item\nF4 - Inserir Quantidade\nF5 - Nova Venda")

        label_tc_1.setStyleSheet("QLabel{background-color:white;font-size:10pt;padding:10px}")

        layout_tc.addWidget(label_tc_1)

        

        label_tc_2 = QLabel("F7 - Pesquisar Venda\nF8 - Pesquisar Produto\nF9 - Alterar Venda\nF10 - Finalizar")

        label_tc_2.setStyleSheet("QLabel{background-color:white;font-size:10pt;padding:10px}")

        layout_tc.addWidget(label_tc_2)

        

        label_tc.setLayout(layout_tc)

        

        label_tc_3 = QLabel("F11 - Exlcuir Venda\nCTRL+D - CPF\nCTRL+P - Preço do Produto\nCTRL+R - Contas Receber")

        label_tc_3.setStyleSheet("QLabel{background-color:white;font-size:10pt;padding:10px}")

        layout_img_v.addWidget(label_tc)

        

        

        label_det_esq_2 = QLabel()

        # label_det_esq_2.setFixedHeight(400)

        label_det_esq_2.setAlignment(Qt.AlignTop)

        

        

        

        #Adiciona um novo layout para os elementos verticais

        layout_ver_esq_2 = QVBoxLayout()

        

        

        #labels e lineEdits

        label_codigo_barras = QLabel("CÓDIGO DE BARRAS")

        label_codigo_barras.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:15pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")

        edit_codigo_barras = QLineEdit()

        edit_codigo_barras.setStyleSheet("QLineEdit{font-size:15pt;text-align:right;padding:10px}")

        

        label_valor_unitario = QLabel("VALOR UNITÁRIO")

        label_valor_unitario.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:15pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")

        edit_valor_unitario = QLineEdit()

        edit_valor_unitario.setStyleSheet("QLineEdit{font-size:15pt;text-align:right;padding:10px}")

        

        label_total_iten = QLabel("TOTAL DO ITEM")

        label_total_iten.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:15pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")

        edit_total_item = QLineEdit()

        edit_total_item.setStyleSheet("QLineEdit{font-size:15pt;text-align:right;padding:10px}")

        

        

        label_total_iten_novo = QLabel("")

        label_total_iten_novo.setStyleSheet("QLabel{background-color:#033c67;color:white;font-size:15pt;font-weight:bold;border-top-left-radius: 10px;border-top-right-radius: 10px;padding:10px}")

        edit_total_item_novo = QLineEdit()

        edit_total_item_novo.setStyleSheet("QLineEdit{font-size:15pt;text-align:right;padding:10px}")

        

        

        

        layout_ver_esq_2.addWidget(label_codigo_barras)

        layout_ver_esq_2.addWidget(edit_codigo_barras)

        

        layout_ver_esq_2.addWidget(label_valor_unitario)

        layout_ver_esq_2.addWidget(edit_valor_unitario)

        

        layout_ver_esq_2.addWidget(label_total_iten)

        layout_ver_esq_2.addWidget(edit_total_item)

        

        layout_ver_esq_2.addWidget(label_total_iten_novo)

        layout_ver_esq_2.addWidget(edit_total_item_novo)

        

        label_tc_3.setFixedHeight(100)

        

        layout_ver_esq_2.addWidget(label_tc_3)  

        #adicionar o layout na label_det_esq_2
        label_det_esq_2.setLayout(layout_ver_esq_2)

        #adicionando as labels no layout_hor_esq_inf
        layout_hor_esq_inf.addWidget(label_det_esq_1_v)
        layout_hor_esq_inf.addWidget(label_det_esq_2)

        # label_det_esq.setFixedHeight(400)

        label_det_esq.setLayout(layout_hor_esq_inf)
    
        # adicionando um novo layout a label na parte inferior
        label_inf_lay_pri.setLayout(layout_lab_inf)

        #adicionando as laybels no layout
        layout_principal.addWidget(label_logo_img)
        layout_principal.addWidget(label_inf_lay_pri)

        #adicionando o layout principal a tela principal
        self.setLayout(layout_principal)

if __name__=="__main__":

    app = QApplication(sys.argv)
    tela = CaixaPDV()
    tela.show()
    app.exec_()



