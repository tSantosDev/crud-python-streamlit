import services.database as db;
import models.fornecedor as fornecedor;

def incluirFornecedor(fornecedor):
    count = db.cursor.execute("""
    INSERT INTO fornecedor (nome_fornecedor, CNPJ) 
    VALUES (?,?)""",
    fornecedor.nome_fornecedor, fornecedor.CNPJ).rowcount
    db.cnxn.commit()

def selecionarIdFornecedor(fornecedor_id):
    db.cursor.execute("SELECT * FROM fornecedor WHERE fornecedor_id = ?", fornecedor_id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(fornecedor.fornecedor(row[0], row[1], row[2]))

    return costumerList[0]      

def alterarFornecedor(fornecedor):
    count = db.cursor.execute("""
    UPDATE fornecedor 
    SET nome_fornecedor = ?, CNPJ = ?
    WHERE fornecedor_id = ?""",
    fornecedor.nome_fornecedor, fornecedor.CNPJ, fornecedor.fornecedor_id).rowcount
    db.cnxn.commit()    

def excluirFornecedor(fornecedor_id):
    count = db.cursor.execute("""
    DELETE FROM fornecedor WHERE fornecedor_id = ?""",
    fornecedor_id).rowcount
    db.cnxn.commit()

def selecionarFornecedor():
    db.cursor.execute("SELECT * FROM fornecedor")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(fornecedor.fornecedor(row[0], row[1], row[2]))

    return costumerList    