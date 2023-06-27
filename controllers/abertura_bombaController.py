import services.database as db;
import models.abertura_bomba as abertura_bomba;

def incluirAberturaBomba(abertura_bomba):
    count = db.cursor.execute("""
    INSERT INTO abertura_bomba (bomba_id, funcionario_id, valor_venda) 
    VALUES (?,?,?)""",
    abertura_bomba.bomba_id, abertura_bomba.funcionario_id, abertura_bomba.valor_venda).rowcount
    db.cnxn.commit()

def selecionarIdAberturaBomba(abertura_bomba_id):
    db.cursor.execute("SELECT * FROM abertura_bomba WHERE abertura_bomba_id = ?", abertura_bomba_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(abertura_bomba.abertura_bomba(row[0], row[1], row[2], row[3]))

    return costumerList[0]      

def alterarAberturaBomba(abertura_bomba):
    count = db.cursor.execute("""
    UPDATE abertura_bomba 
    SET bomba_id = ?, funcionario_id = ?, valor_venda = ?
    WHERE abertura_bomba_id = ?""",
    abertura_bomba.bomba_id, abertura_bomba.funcionario_id, abertura_bomba.valor_venda, abertura_bomba.abertura_bomba_id).rowcount
    db.cnxn.commit()    

def excluirAberturaBomba(abertura_bomba_id):
    count = db.cursor.execute("""
    DELETE FROM abertura_bomba WHERE abertura_bomba_id = ?""",
    abertura_bomba_id).rowcount
    db.cnxn.commit()

def selecionarAberturaBomba():
    db.cursor.execute("SELECT * FROM abertura_bomba")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(abertura_bomba.abertura_bomba(row[0], row[1], row[2], row[3]))

    return costumerList    