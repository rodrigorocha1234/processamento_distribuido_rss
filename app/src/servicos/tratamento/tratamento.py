import re
from typing import List

from bs4.element import ResultSet


class Tratamento:

    @staticmethod
    def limpar_descricao(textos: ResultSet) -> str:
        """
        Método para limpar o texto da notícia e criar parágrafos a cada ponto.

        Args:
            textos (ResultSet): Conteúdo do texto HTML da notícia, lista de elementos Tag.

        Returns:
            str: Texto limpo, com parágrafos separados por pontos.
        """
        lista_texto: List[str] = []

        for elemento in textos:
            if (not elemento.find('ul') and not elemento.find('div',
                                                              class_='content-intertitle') and "LEIA TAMBÉM:" not in (
                    elemento.text or '')):
                texto_extraido = (elemento.text or '').strip()
                lista_texto.append(texto_extraido)

        padroes_a_remover = [
            # LEIA TAMBÉM
                r"\bLEIA\s+TAMB[ÉE]M\s*:?",

                # WhatsApp (Ribeirão e Franca)
                r"(?:✅\s*)?"
                r"(?:Clique\s+)?aqui\s+para\s+seguir\s+o\s+canal\s+do\s+g1\s+"
                r"Ribeir[aã]o(?:\s+Preto)?\s+e\s+Franca\s+no\s+WhatsApp\.?",

                # WhatsApp (Pará)
                r"(?:✅\s*)?"
                r"(?:Clique\s+)?aqui\s+para\s+seguir\s+o\s+canal\s+do\s+g1\s+"
                r"Par[aá]\s+no\s+WhatsApp\.?",

                # Forma abreviada: "Siga o canal..."
                r"(?:✅\s*)?"
                r"Siga\s+o\s+canal\s+do\s+g1\s+"
                r"(?:Par[aá]|Ribeir[aã]o(?:\s+Preto)?\s+e\s+Franca)"
                r"\s+no\s+WhatsApp\.?",

                # Veja mais notícias...
                r"Veja\s+mais\s+not[ií]cias\s+da\s+regi[aã]o\s+no\s+g1\s+"
                r"Ribeir[aã]o(?:\s+Preto)?\s+e\s+Franca\.?",

                # VÍDEOS:
                r"V[ÍI]DEOS\s*:\s*Tudo\s+sobre\s+Ribeir[aã]o\s+Preto,\s*"
                r"Franca\s+e\s+regi[aã]o\.?",

        ]

        texto_completo = '\n\n'.join(lista_texto)

        texto_limpo = texto_completo
        for padrao in padroes_a_remover:
            texto_limpo = re.sub(padrao, '', texto_limpo, flags=re.IGNORECASE)

        return texto_limpo
