# Brasil - Feriados Nacionais
Serviço de Consulta aos Feriados Nacionais do Brasil.

## Feriados Fixos

Data | Evento
---|---
01/01 | Ano Novo
21/04 | Tiradentes
01/05 | Dia do Trabalho
07/09 | Independência do Brasil
12/10 | Nossa Senhora Aparecida
02/11 | Finados
15/11 | Proclamação da República
25/12 | Natal
20/11 | Dia da Consciência Negra (à partir de 2023)

## Feriados Móveis

Os feriados móveis são baseados no dia de páscoa.

[Wikipédia - Cálculo da Páscoa](https://pt.wikipedia.org/wiki/C%C3%A1lculo_da_P%C3%A1scoa)

Neste projeto, foi utilizado o algoritmo de Meeus/Jones/Butcher.

O objetivo é identificar o dia da páscoa do ano desejado e calcular os outros eventos à partir desse dia, da seguinte forma:

Evento | Referência
---|---
Páscoa | Algoritmo
Carnaval | Páscoa - 47 dias
Sexta-feira Santa | Páscoa - 2 dias
Corpus Christi | Páscoa + 60 dias
