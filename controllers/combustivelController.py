import services.database as db;
import models.combustivel as Combustivel;

def incluirCombustivel(combustivel):
    count = db.cursor.execute("""
    INSERT INTO combustivel (nome_combustivel, estoque, preco_venda, preco_compra, fornecedor_id) 
    VALUES (?,?,?,?,?)""",
    combustivel.nome_combustivel, combustivel.estoque, combustivel.preco_venda, combustivel.preco_compra, combustivel.fornecedor_id).rowcount
    db.cnxn.commit()

def selecionarIdCombustivel(combustivel_id):
    db.cursor.execute("SELECT * FROM combustivel WHERE combustivel_id = ?", combustivel_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(Combustivel.combustivel(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList[0]      

def alterarCombustivel(combustivel):
    count = db.cursor.execute("""
    UPDATE combustivel 
    SET nome_combustivel = ?, estoque = ?, preco_venda = ?, preco_compra = ?, fornecedor_id = ?
    WHERE combustivel_id = ?""",
    combustivel.nome_combustivel, combustivel.estoque, combustivel.preco_venda, combustivel.preco_compra, combustivel.fornecedor_id, combustivel.combustivel_id).rowcount
    db.cnxn.commit()    

def excluirCombustivel(combustivel_id):
    count = db.cursor.execute("""
    DELETE FROM combustivel WHERE combustivel_id = ?""",
    combustivel_id).rowcount
    db.cnxn.commit()

def selecionarCombustivel():
    db.cursor.execute("SELECT * FROM combustivel")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(Combustivel.combustivel(row[0], row[1], row[2], row[3], row[4], row[5]))

    return costumerList    
