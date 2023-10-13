from django.db import models

# Create your models here.

# Aqui estamos criando toda interface de banco de dados no nosso Django Admin

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places= 2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(default="")
    # Nomeando a classe dentro do banco
    class Meta:
        verbose_name_plural = "Transacoes"
    def __str__(self):
        return self.descricao
    