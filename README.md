# Documentació oficial

**Taula de continguts**

</br>

[TOC]

### Descripció del meu joc

<p>Es tracta d'un joc d'estil minimalista, que funciona fent interaccions mitjançant el botó esquerre del ratoli, que implementa diverses funcionalitats, per exemple, 
quan fas 20 atacs s'afegeix un nou atac anomenat "rayo" que compta per 2, però l'atac bàsic "placaje" té un extra que et genera coins del joc
per tal de aconseguir/comprar recursos a la tenda que et podran facilitar la partida. Cada recurs de la tenda té un cost de 20/25 coins. </p>
<p>Guanyaràs la partida quan, arribis a Mewtwo i facis un total de 60 atacs. (visualitzable a pantalla.) </p>
<p>Perdràs quan el cronometre arribi a 0.</p>

### Controls del joc

<p>La dinàmica del joc és anar guanyant combats mitjançant el clic del ratolí. </p>
<p>Hi ha dos combats més un pokemon final.</p> 
<p> Per lluitar, i fer qualsevol acció, haurem de fer clic amb el botó esquerre del ratolí. ( si prems el botó dret no compta)</p>

### Funcionalitats

#### Atacs
<p>Els podem fer amb el clic dret del ratolí.</p>

<p>El primer atac que hi ha 'Placaje' que compta 1 clic. </p>

<p>Quan arribem als 20 o més clics totals, s'habilitarà un segon atac especial anomenat 'Rayo', que compta per dos clics.</p>

#### Guanyem o perdrem?
<p>Guanyarem el primer combat quan fem <strong>15 clics</strong>.</p>
<p>El segon combat el guanyarem quan fem <strong>30 clics (totals)</strong>.</p> 
<p>Guanyarem la partida fent un total de <strong>60 clics</strong> (guanyant al pokemon final).</p>
<p> Perdrem quan, el temporitzador, fent el compte enrere, arribi a 0. Tens un total de 100 segons pels tres combats.</p>

#### Tenda del joc

<p>Al lateral dret, tenim la tenda del joc. Hi ha dos elements instal·lats:</p>
<ul>
<li>Poció: Es compra per <strong>20 coins</strong>. El seu funcionament és afegir 10 segons al temporitzador.</li></br>
<li>Caramel +DEF: Es compra per <strong>25 coins</strong>. El seu funcionament és donar-li "delay" al temporitzador.</li></ul>
<p>Per adquirir "coins" has de fer atacs bàsics, és a dir, clic a "placaje", que compta per 1 clic, i així premies fer els dos atacs.   

#### Restriccions demanades

##### Requeriments funcionals
<ul>
<li>El jugador pot interaccionar amb l'entorn per adquirir recursos. (Tenda al lateral dret).</li>

<li>Recursos adquiribles automàticament: quan fas atacs amb "placaje" vas adquirint 2 coins per clic. que són les monedes amb les quals compres recursos.</li>

<li>Elements desbloquejables i augmentables: segon atac especial, i els elements de la tenda.</li>

<li>Informació sobre el joc a pantalla: Atacs totals, temporitzador, recursos...</li>

<li>Mínim 2 pantalles operatives: Hi ha 3 pantalles operatives. A partir de la segona ronda, canvia de color del gris inicial al marró.</p>

<li>Objectiu: El joc s'acaba quan guanyem al pokemon final. i ens surtirà una finestra nova de guanyadors amb un historial de pokemons guanyats. També hi ha una pantalla en cas de perdre.</li>

<li>Pantalla de presentació amb opció de jugar i sortir.</li>

</ul>

##### Requeriments tècnics

<ul>
<li>El codi implementat utilitzant funcions per tal que sigui modular.</li>
<li>Gestió de memòria eficient.</li>
<li>Codi font desat i pujat diariament a gitlab</li>
<li>El joc s'executa sense errors</li>
<li>Opció d'accelerar l'acumulació de recursos: segon atac "rayo" que compta per tres clics.</li>
</ul>
