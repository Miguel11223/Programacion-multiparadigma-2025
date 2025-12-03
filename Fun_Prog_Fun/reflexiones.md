# Parte 1

## Función A  

**Es pura**, esto debido a que esta es determinista y no modifica ninguna variable.

## Función B  

**Es impura**, debido a que modifica el estado de la variable contador y además el resultado depende de cuántas veces se haya llamado a la función.

**Para hacer su versión pura** se debe de recibir el contador como argumento y devolver el nuevo junto al id que se generó.

## Función C  

**Es impura**, debido a que modifica el registro que usa de argumento y la hora siempre será diferente cada vez que es llamada.

**Para hacer su versión pura** se debe de crear una copia de registro antes de modificarlo y además recibir la fecha como un argumento.

## Función D  

**Es pura** ya que es determinista y no modifica la lista original si no que genera otra nueva.

## Función E  

**Es impura**, ya que modifica el orden de la lista original y utiliza un random que hará que con cada ejecución sea distinto el resultado.

**Para su versión pura** se debe de crear una copia de la lista antes mezclarla y además tal vez agregar una función que se encargue de realizar la mezcla de las listas.
