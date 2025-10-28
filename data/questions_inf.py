questions2ADAC_INF = {
    # HTTP Request-Response Fragen
    "Worauf lässt sich der Erfolg des WWW zurückführen?": {
        "a": "Das WWW wurde für eine benutzerfreundliche Möglichkeit entwickelt, einfach an Informationen zu kommen. Außerdem kann durch offene Standards jeder Webseiten erstellen.",
        "b": "Das WWW basiert auf proprietären Standards, die nur von wenigen genutzt werden können.",
        "c": "Das WWW wurde entwickelt, um nur Textinformationen zu übertragen.",
        "correct": "a"
    },
    "Was versteht man unter dem Request-Response-Schema?": {
        "a": "Der Server stellt eine Anfrage (Request) an den Client und der Client antwortet (Response).",
        "b": "Als Client stellt man eine Anfrage (Request) an einen Server, der einem Informationen liefern soll. Diese Anfrage enthält meist Details, was für Informationen verlangt werden (z.B GET/POST-Methoden). Darauf sendet der Server eine Antwort (Response), ob die Informationen erfolgreich überbracht wurden. Diese werden in Statuscodes an den Client überbracht.",
        "c": "Request-Response-Schema beschreibt den Austausch von Dateien zwischen zwei Servern.",
        "correct": "b"
    },
    "Worauf war die ursprüngliche Version von HTTP ausgerichtet?": {
        "a": "Auf die Übertragung von Bildern.",
        "b": "Auf die Übertragung von Hypertextdokumenten zwischen Server und Client.",
        "c": "Auf die Übertragung von Audio und Video.",
        "correct": "b"
    },
    "Wie können seit HTTP 1.1 in beide Richtungen mehr Informationen übergeben werden?": {
        "a": "Durch die Einführung von verschlüsselten Verbindungen.",
        "b": "Durch die Einführung von Headern und Cookies.",
        "c": "Durch die Verwendung von XML.",
        "correct": "b"
    },
    "Was bringt die Möglichkeit persistenter Verbindungen?": {
        "a": "Erhöhte Wartezeiten und Ressourcenverbrauch.",
        "b": "Die Notwendigkeit, für jede Anfrage eine neue Verbindung aufzubauen.",
        "c": "Sparung von Wartezeiten und effizientere Nutzung von Ressourcen.",
        "correct": "c"
    },
    "Beschreiben Sie den Ablauf einer HTTP-Verbindung (textuell oder grafisch)": {
        "a": "Der Server sendet eine Anfrage an den Client, der Client antwortet, und die Verbindung wird geschlossen.",
        "b": "Der Client öffnet eine TCP-Verbindung zum Server, stellt eine HTTP-Anfrage, der Server antwortet mit einem Statuscode und der Inhalt wird gerendert. Bei persistenten Verbindungen bleibt die Verbindung bestehen.",
        "c": "Der Client stellt eine Anfrage an den DNS-Server, der die IP-Adresse des Webservers liefert.",
        "correct": "b"
    },
    "Was bewirkt eine HTTP-Methode ohne Angabe eines Ziels?": {
        "a": "Die Anfrage ist erfolgreich, aber es wird keine Antwort gesendet.",
        "b": "Die HTTP-Anfrage ist unvollständig und führt zu einem fehlerhaften Request.",
        "c": "Der Server führt eine Standardaktion aus.",
        "correct": "b"
    },
    "Erklären Sie den Begriff Status-Code im Zusammenhang mit dem HTTP-Response.": {
        "a": "Status-Codes geben den Erfolg oder Misserfolg einer Anfrage an und werden in 5 Klassen unterteilt: 1xx, 2xx, 3xx, 4xx, 5xx.",
        "b": "Status-Codes sind nur bei Fehlermeldungen relevant.",
        "c": "Status-Codes werden verwendet, um die Geschwindigkeit einer Anfrage zu messen.",
        "correct": "a"
    },
    "Was versteht man unter einer Reason-Phrase im HTTP-Response?": {
        "a": "Eine Reason-Phrase ist ein numerischer Code, der den Erfolg einer Anfrage anzeigt.",
        "b": "Die Reason-Phrase beschreibt kurz, für was der jeweilige Statuscode steht.",
        "c": "Eine Reason-Phrase ist ein spezieller Header in HTTP-Anfragen.",
        "correct": "b"
    },
    "Was versteht man unter einer HTTP-Methode?": {
        "a": "Eine HTTP-Methode beschreibt, welche Aktion der Client versucht, auszuführen, wie GET oder POST.",
        "b": "Eine HTTP-Methode ist ein Sicherheitsprotokoll für Webanfragen.",
        "c": "Eine HTTP-Methode ist ein Netzwerkprotokoll für den Datenaustausch.",
        "correct": "a"
    },
    "Für was wird die HTTP-GET-Methode verwendet?": {
        "a": "Um Daten zum Server zu senden und neue Ressourcen zu erstellen.",
        "b": "Um Daten einer Ressource anzufordern.",
        "c": "Um eine bestehende Ressource zu löschen.",
        "correct": "b"
    },
    "Für was wird die HTTP-POST-Methode verwendet?": {
        "a": "Um Daten einer Ressource anzufordern.",
        "b": "Um eine bestehende Ressource zu löschen.",
        "c": "Um Daten zum Server zu senden und neue Ressourcen zu erstellen.",
        "correct": "c"
    },

    # HTML Teil 1 Fragen
    "Nennen Sie mind. 3 Themenbereiche für eine Webseite:": {
        "a": "E-Commerce, Information, Unternehmen",
        "b": "Sport, Freizeit, Mode",
        "c": "Reisen, Musik, Kunst",
        "correct": "a"
    },
    "Wie könnte man eine Webseite zum Geld verdienen nutzen?": {
        "a": "Durch Platzieren von Anzeigen und Affiliate-Links.",
        "b": "Durch das Vermeiden von Werbung.",
        "c": "Durch das kostenlose Anbieten aller Inhalte.",
        "correct": "a"
    },
    "Wie werden HTML-Tags geschrieben, was beschreibt ein HTML-Tag?": {
        "a": "Ein HTML-Tag enthält einen Tagnamen innerhalb von runden Klammern (()), der Inhalt des Tags steht zwischen einem Öffnungstag (tag) und einem Schließtag (/tag).",
        "b": "Ein HTML-Tag enthält einen Tagnamen innerhalb von eckigen Klammern ([]), der Inhalt des Tags steht zwischen einem Öffnungstag ([tag]) und einem Schließtag ([/tag]).",
        "c": "Ein HTML-Tag enthält einen Tagnamen innerhalb von spitzen Klammern (<>), der Inhalt des Tags steht zwischen einem Öffnungstag (<tag>) und einem Schließtag (</tag>).",
        "correct": "c"
    },
    "Was ist die Hauptaufgabe des Browsers?": {
        "a": "Die Webseiteninhalte korrekt darzustellen.",
        "b": "Die Webseiteninhalte zu blockieren.",
        "c": "Die Webseiteninhalte zu speichern.",
        "correct": "a"
    },
    "Was versteht man im Zusammenhang mit Browsern unter 'Rendering'?": {
        "a": "Das Blockieren von Werbung auf Webseiten.",
        "b": "Das Interpretieren von HTML-/CSS-/JavaScript-Code und die darauffolgende Darstellung der Inhalte vom Webserver.",
        "c": "Das Speichern von Webseiteninhalten auf dem Server.",
        "correct": "b"
    },
    "Wodurch entstehen geräteabhängige Unterschiede bei der Anzeige von Webseiten?": {
        "a": "Durch unterschiedliche Bildschirmauflösungen/-größen, Browserkompatibilität und Betriebssysteme.",
        "b": "Durch die Internetgeschwindigkeit des Nutzers.",
        "c": "Durch die Farbeinstellungen des Monitors.",
        "correct": "a"
    },
    "Wodurch entstehen herstellerabhängige Unterschiede bei der Anzeige von Webseiten?": {
        "a": "Durch verschiedene Browser-Engines, Webstandards oder neuwertige Funktionen, die nicht jeder Browser unterstützt.",
        "b": "Durch die Internetgeschwindigkeit des Nutzers.",
        "c": "Durch die Farbeinstellungen des Monitors.",
        "correct": "a"
    },
    "Welche Unterschiede können durch unterschiedliche Betriebssysteme erfolgen?": {
        "a": "Durch die Farbgebung der Benutzeroberfläche.",
        "b": "Durch die Art, wie Schriftarten gerendert werden oder ob sie vorhanden sind, sowie verschiedene UI-Stile und Dateisysteme.",
        "c": "Durch die Bildschirmauflösung.",
        "correct": "b"
    },
    "Welche Vorteile entstehen durch die Nutzung von HTML und CSS?": {
        "a": "HTML und CSS verbessern die Ladezeit von Webseiten drastisch.",
        "b": "HTML und CSS garantieren Konsistenz von Regeln und Anpassungsfähigkeit. Getrennte CSS-Inhalte machen den Code lesbarer und verbessern die Suchmaschinenoptimierung.",
        "c": "HTML und CSS verhindern, dass Webseiten gehackt werden.",
        "correct": "b"
    },

    # HTML Teil 2 Fragen
    "Was versteht man in der Web-Entwicklung unter mobile-first?": {
        "a": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung zuerst für Desktop-Computer optimiert werden.",
        "b": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung zuerst für mobile Endgeräte optimiert werden.",
        "c": "Ansatz der Web-Entwicklung, bei dem das Design und die Entwicklung einer Website oder Anwendung gleichzeitig für alle Gerätetypen optimiert werden.",
        "correct": "b"
    },
    "Was ist die Stärke von Flexbox in CSS?": {
        "a": "Flexbox kann komplexe Layouts auf einfache und flexible Weise erstellen. Vorteile sind zudem Responsive Design, das leichte Anordnen von Elementen und die Verteilung von Platz zwischen und innerhalb von Elementen.",
        "b": "Flexbox ist speziell für die Gestaltung von Tabellen gedacht.",
        "c": "Flexbox ist hauptsächlich für die Gestaltung von Formularen nützlich.",
        "correct": "a"
    },
    "Welche Arten von 'Links' gibt es?": {
        "a": "Text-Link, Bild-Link, Video-Link, Audio-Link",
        "b": "Text-Link, Bild-Link, E-Mail-Link, Telefonnummer-Link, Verweis auf ein Dokument, Verweis auf eine externe Webseite",
        "c": "Text-Link, Dokument-Link, Script-Link, PDF-Link",
        "correct": "b"
    },
    "Nennen Sie ein Argument warum verbundene Zellen innerhalb einer HTML-Table vermeiden soll?": {
        "a": "Verbundene Zellen machen die Tabelle hübscher.",
        "b": "Verbundene Zellen können die Struktur der Daten verzerren und die Zugänglichkeit beeinträchtigen, z.B bei Screenreadern.",
        "c": "Verbundene Zellen verbessern die Ladezeit der Tabelle.",
        "correct": "b"
    },
    "Wie sind HTML-Tabellen aufgebaut?": {
        "a": "<table>-Tag am Anfang, <tr>-Tag (Table Row) für Tabellenzeile, <td>-Tag (Table Data) für Inhalt der Zelle, <th> (Table Header) für Überschriften. Wahlweise mit <thead>, <tbody> und <tfoot> ergänzen.",
        "b": "<table>-Tag am Anfang, <row>-Tag für Tabellenzeile, <cell>-Tag für Inhalt der Zelle, <header> für Überschriften.",
        "c": "<table>-Tag am Anfang, <line>-Tag für Tabellenzeile, <data>-Tag für Inhalt der Zelle, <head> für Überschriften.",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen einer 'id' und einer 'class'. Wie würde der CSS-Selektor für class='ziel' bzw. id='ziel' aussehen?": {
        "a": "Die 'id' ist ein eindeutiger Bezeichner für ein bestimmtes Element, während 'class' eine Gruppe von Elementen kennzeichnet. CSS-Selektor für id='ziel': .ziel, für class='ziel': #ziel.",
        "b": "Die 'id' ist ein Bezeichner für eine Gruppe von Elementen, während 'class' ein eindeutiger Bezeichner für ein bestimmtes Element ist. CSS-Selektor für id='ziel': #ziel, für class='ziel': .ziel.",
        "c": "Die 'id' ist ein eindeutiger Bezeichner für ein bestimmtes Element, während 'class' eine Gruppe von Elementen kennzeichnet. CSS-Selektor für id='ziel': #ziel, für class='ziel': .ziel.",
        "correct": "c"
    },
    "Nennen Bildformate mit verlustbehafteter Kompression? Welcher Vorteil wird welchem Nachteil bei Kompression entgegengestellt?": {
        "a": "JPEG, PNG, SVG: Vorteil: bessere Farbtreue, Nachteil: größere Dateigröße.",
        "b": "JPEG, WebP, GIF: Vorteil: Dateigröße wird erheblich reduziert, Nachteil: Qualitätsverlust im Bild, bei starken Kompressionsraten Unschärfen.",
        "c": "JPEG, BMP, TIFF: Vorteil: höhere Auflösung, Nachteil: längere Ladezeiten.",
        "correct": "b"
    },
    "Erklären Sie den Begriff Status-Code im Zusammenhang mit dem HTTP-Response.": {
        "a": "Der Status-Code beschreibt eine numerische Kennzeichnung, die den Zustand einer Anfrage an den Server widerspiegelt. Die erste Ziffer des Status-Codes gibt die allgemeine Kategorie des Status an: 1xx: Informational, 2xx: Success, 3xx: Redirection, 4xx: Client Error, 5xx: Server Error.",
        "b": "Der Status-Code beschreibt die Geschwindigkeit einer Anfrage an den Server.",
        "c": "Der Status-Code gibt an, welche Datei auf dem Server angefragt wurde.",
        "correct": "a"
    },
    "Was versteht man bei Bildern unter Transparenz? Bei welchen Bildformaten ist dies möglich?": {
        "a": "Transparenz bezieht sich darauf, dass es einen transparenten Hintergrund gibt, sodass der darunterliegende Inhalt sichtbar ist. Transparenz ist bei PNG, GIF, SVG und WebP möglich.",
        "b": "Transparenz bezieht sich auf die Fähigkeit eines Bildes, ohne Qualitätsverlust zu komprimieren. Transparenz ist bei JPEG, BMP und TIFF möglich.",
        "c": "Transparenz bezieht sich auf die Möglichkeit, ein Bild in verschiedenen Farbtiefen darzustellen. Transparenz ist bei BMP, TIFF und RAW möglich.",
        "correct": "a"
    },
}
questions3ADAC_INF = {
    "Welche wichtigen Gründe führten zur Entwicklung von Datenbanksystemen?": {
        "a": "Speicherung von Daten auf Papier",
        "b": "Vereinfachung der Hardwarekonfiguration",
        "c": "Verwaltung von großen Datenmengen und Reduzierung von Redundanzen",
        "correct": "c"
    },
    "Was sind Redundanzen in Datenbanken?": {
        "a": "Wiederholte Daten, die mehrfach ohne Notwendigkeit gespeichert sind",
        "b": "Eindeutige Daten, die nur einmal gespeichert sind",
        "c": "Daten, die immer auf die gleiche Weise abgefragt werden",
        "correct": "a"
    },
    "Was sind Inkonsistenzen in Datenbanken?": {
        "a": "Daten, die immer korrekt sind",
        "b": "Widersprüchliche oder unvollständige Daten",
        "c": "Eindeutige und konsistente Datenbeziehungen",
        "correct": "b"
    },
    "Was ist ein Mehrnutzerbetrieb in Datenbanken?": {
        "a": "Das Speichern von Daten auf einem einzelnen Rechner",
        "b": "Das gleichzeitige Arbeiten mehrerer Nutzer an der Datenbank",
        "c": "Das Arbeiten mit einer einzigen Benutzeroberfläche",
        "correct": "b"
    },
    "Welche Probleme können im Mehrnutzerbetrieb auftreten?": {
        "a": "Vollständige Datenkonsistenz",
        "b": "Keine Fehler bei Datenbankoperationen",
        "c": "Datenkonflikte und Zugriffsprobleme",
        "correct": "c"
    },
    "Was ist ein Datenbankmanagementsystem (DBMS)?": {
        "a": "Ein Netzwerk zur Verbindung von Datenbanken",
        "b": "Ein System zur physikalischen Speicherung von Daten",
        "c": "Ein Softwarepaket, das die Verwaltung der Datenbank und den Zugriff auf Daten regelt",
        "correct": "c"
    },
    "Welche Aufgaben hat ein DBMS?": {
        "a": "Stellt nur den Zugriff auf Daten zur Verfügung",
        "b": "Verarbeitet nur Datenbankabfragen",
        "c": "Stellt Daten zur Verfügung, gewährleistet Datenintegrität und Datensicherung",
        "correct": "c"
    },
    "Was ist ein Data Dictionary?": {
        "a": "Ein physisches Speichermedium für Daten",
        "b": "Ein Werkzeug zur Überwachung von Datenbankabfragen",
        "c": "Ein Datenlexikon, das Informationen über Datenbankobjekte speichert",
        "correct": "c"
    },
    "Welche Datenbankmodelle kennen Sie?": {
        "a": "Nur hierarchische und Netzwerk-Datenbanken",
        "b": "Nur relationale Datenbanken",
        "c": "Hierarchische, Netzwerk-, Relationale-, Spaltenorientierte-, Dokumentorientierte-, Objektorientierte- und NoSQL-Datenbanken",
        "correct": "c"
    },
    "Was ist das hierarchische Datenbankmodell?": {
        "a": "Daten werden in einer baumartigen Struktur mit eindeutigen Eltern-Kind-Beziehungen gespeichert",
        "b": "Daten werden als Objekte mit Attributen und Methoden gespeichert",
        "c": "Daten werden in einer flachen Struktur ohne Beziehungen gespeichert",
        "correct": "a"
    },
    "Was ist das relationale Datenbankmodell?": {
        "a": "Daten werden in einer baumartigen Struktur organisiert",
        "b": "Daten werden als Objekte mit Attributen und Methoden gespeichert",
        "c": "Daten werden in Tabellen gespeichert und durch Primär- und Fremdschlüssel miteinander verknüpft",
        "correct": "c"
    },
    "Welche physischen Datenbankarchitekturen gibt es?": {
        "a": "Nur zentralisierte DBS",
        "b": "Zentralisierte DBS, Verteilte DBS, Client-Server DBS, Parallele DBS",
        "c": "Nur verteilte und parallele DBS",
        "correct": "b"
    },
    "Was ist eine zentrale Datenbankarchitektur?": {
        "a": "Datenbanken sind auf mehreren geografisch entfernten Servern verteilt",
        "b": "Das gesamte DBMS und die Anwendungen sind auf einem einzelnen Rechner gespeichert",
        "c": "Daten werden auf mehreren Prozessoren gleichzeitig verarbeitet",
        "correct": "b"
    },
    "Was ist das Client-Server-Modell in Datenbanken?": {
        "a": "Ein Modell, bei dem alle Daten auf einem zentralen Server gespeichert werden",
        "b": "Ein System, bei dem zwei unabhängige Prozesse über eine Schnittstelle miteinander kommunizieren",
        "c": "Ein Modell, das mehrere physische Speicherorte für Daten nutzt",
        "correct": "b"
    },
    "Was ist eine Relation bzw. Was beschreibt Sie? Führen Sie drei Eigenschaften an.": {
        "a": "Eine Menge von Tupeln in Form einer Tabelle mit Spalten und Zeilen. Eigenschaften: Eindeutiger Name, mehrere Attribute, Primärschlüssel.",
        "b": "Eine Sammlung von Tabellen mit unterschiedlichen Datentypen und Formaten.",
        "c": "Eine Reihe von Spalten, die miteinander verknüpft sind.",
        "correct": "a"
    },
    "Was versteht man unter funktionaler Abhängigkeit? (mit eigenen Worten)": {
        "a": "Es gibt eine Beziehung, in der sich bestimmte Daten aufgrund eines anderen Wertes ändern.",
        "b": "Eine funktionale Abhängigkeit beschreibt, wie sich Datensätze im Laufe der Zeit verändern.",
        "c": "Die Funktionale Abhängigkeit besagt, dass ein Wert X immer einen anderen Wert Y beeinflusst, der sich nicht ändern kann.",
        "correct": "c"
    },
    "Was versteht man unter transitiver Abhängigkeit?": {
        "a": "Attribute sind in einer Kette zwischen anderen Attributen voneinander abhängig.",
        "b": "Es gibt eine direkte Beziehung zwischen Attributen, ohne Zwischenwerte.",
        "c": "Ein Attribut ist von einem anderen Attribut direkt abhängig, ohne Zwischenstationen.",
        "correct": "a"
    },
    "Was sind die Ziele der Normalisierung? Mind. 3.": {
        "a": "Verhindert Datenredundanz, Verhindert Dateninkonsistenz, Stellt eine einfache Datensicherung sicher.",
        "b": "Verhindert Redundanzen, Gewährleistet die Vollständigkeit der Datenbank, Macht Daten schwer zugänglich.",
        "c": "Verhindert Datenredundanz, Verhindert Dateninkonsistenz, Sicherheit bei Einfügen, Löschen oder Ändern von Datensätzen.",
        "correct": "c"
    },
    "Beschreiben Sie die 1:1 Beziehung und führen Sie ein Beispiel an:": {
        "a": "Ein Tupel aus einer Relation ist genau einem Tupel aus einer anderen Relation zugeordnet.",
        "b": "Ein Tupel aus einer Relation kann mehreren Tupeln aus einer anderen Relation zugeordnet sein.",
        "c": "Ein Tupel ist in keiner Weise mit anderen Tupeln verknüpft.",
        "correct": "a"
    },
    "Beschreiben Sie die 1:n Beziehung": {
        "a": "Jede Entität einer Entitätsmenge ist einer oder mehreren Entitäten einer anderen Entitätsmenge zugeordnet.",
        "b": "Jede Entität ist nur mit genau einer anderen Entität einer anderen Menge verbunden.",
        "c": "Jede Entität ist mit mehreren Entitäten aus der gleichen Entitätsmenge verbunden.",
        "correct": "a"
    },
    "Was ist ein Primärschlüssel?": {
        "a": "Ein Primärschlüssel ist ein eindeutiger Identifikator für eine Entität einer Entitätsmenge, dessen Wert nur einmal vorkommen kann.",
        "b": "Ein Primärschlüssel ist ein allgemeiner Identifikator, der nicht unbedingt eindeutig ist.",
        "c": "Ein Primärschlüssel ist ein sekundärer Schlüssel, der von anderen Tabellen referenziert wird.",
        "correct": "a"
    },
    "Was ist ein Fremdschlüssel?": {
        "a": "Ein Fremdschlüssel ist der Identifikator einer Fremd-Relation, der in der aktuellen Relation eingebunden wird, um eine Beziehung einzugehen.",
        "b": "Ein Fremdschlüssel ist ein Wert, der nur für die interne Nutzung innerhalb einer Tabelle verwendet wird.",
        "c": "Ein Fremdschlüssel ist ein genereller Schlüssel, der alle Daten einer Tabelle referenziert.",
        "correct": "a"
    },
    "Was versteht man unter NULL-Werten oder leeren Einträgen?": {
        "a": "NULL-Werte beschreiben die Abwesenheit von Werten, während leere Einträge mit einem Standardwert versehen sind.",
        "b": "Leere Einträge sind Werte, die vollständig fehlen, NULL-Werte sind Standardwerte.",
        "c": "NULL-Werte und leere Einträge sind dasselbe und können ohne Unterschied verwendet werden.",
        "correct": "a"
    },
    "Was ist eine Lösch-Anomalie?": {
        "a": "Wenn beim Löschen eines Datensatzes abhängige Datensätze mitgelöscht werden, ohne dass diese gesichert sind.",
        "b": "Wenn durch das Löschen eines Datensatzes alle Referenzen zu diesem Datensatz entfernt werden.",
        "c": "Wenn ein Datensatz durch ein Löschverfahren korrigiert wird.",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 1. Normalform?": {
        "a": "Eine Relation befindet sich in der ersten Normalform, wenn jedes Attribut atomar ist und nur ein Wert pro Tupel erlaubt ist.",
        "b": "Eine Relation ist in der ersten Normalform, wenn alle Werte in einer Tabelle einmalig sind.",
        "c": "Eine Relation in der ersten Normalform erfordert keine Attribute mit mehreren Werten.",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 2. Normalform?": {
        "a": "Wenn die 1. Normalform erfüllt ist und jedes Nicht-Schlüsselfeld vom Primärschlüssel abhängt.",
        "b": "Wenn die Relation keine redundanten Daten enthält.",
        "c": "Wenn jedes Attribut einer Tabelle atomar ist und keine transitiven Abhängigkeiten vorhanden sind.",
        "correct": "a"
    },
    "Was versteht man unter einer Tabelle?": {
        "a": "Eine Tabelle ist nur eine Sammlung von Zahlen ohne Zusammenhang",
        "b": "Eine Tabelle enthält nur Textinformationen ohne Spaltenstruktur",
        "c": "Eine Tabelle besteht aus Zeilen und Spalten, wobei die Zeilen einen Datensatz angeben und die Spalten die Attribute definieren",
        "correct": "c"
    },
    "Aus was bestehen Tabellen und was bewirken diese Bestandteile?": {
        "a": "Tabellen bestehen nur aus Datensätzen ohne Felder",
        "b": "Tabellen bestehen aus Formeln, die automatisch Werte berechnen",
        "c": "Tabellen bestehen aus Feldern/Spalten. Zusammengehörige Daten werden in eine Zeile geschrieben, sie bilden einen Datensatz",
        "correct": "c"
    },
    "Führen Sie ein syntaktisches Beispiel für die Erstellung einer Tabelle für Produkte an. (mitsamt Feldern)": {
        "a": "CREATE TABLE produkte (produktname CHAR, produktid FLOAT);",
        "b": "INSERT INTO produkte VALUES (1, 'Tisch', 'Holztisch');",
        "c": "CREATE TABLE produkte ( id INT NOT NULL PRIMARY KEY, name VARCHAR(100), beschreibung VARCHAR(500));",
        "correct": "c"
    },
    "Beschreiben Sie den Wert NULL und den Umgang damit": {
        "a": "NULL ist gleich 0 und kann in Berechnungen verwendet werden",
        "b": "NULL ist ein Textwert, der leer angezeigt wird",
        "c": "NULL beschreibt eine standardmäßige Leerstelle eines Datenfelds, der Datensatz darf keinen Wert enthalten",
        "correct": "c"
    },
    "Was bewirkt folgende Angabe bei der Erstellung einer Tabelle: “id INTEGER NOT NULL”?": {
        "a": "Die Spalte id wird automatisch als Text gespeichert",
        "b": "Die Spalte id wird als INTEGER erstellt und ein Wert muss eingegeben werden",
        "c": "Die Spalte id darf keine Werte enthalten",
        "correct": "b"
    },
    "Welche Datentypen für ganzzahlige Werte kennen Sie? Wie sind die Wertebereiche dafür?": {
        "a": "CHAR, VARCHAR, TEXT",
        "b": "FLOAT, DOUBLE, NUMERIC",
        "c": "SMALLINT -32768 bis +32767, INTEGER -2147483648 bis +2147483647, BIGINT -9223372036854775808 bis +9223372036854775808",
        "correct": "c"
    },
    "Für was eignen sich numerische Datentypen für Festkommazahlen?": {
        "a": "Für Textinformationen",
        "b": "Nur für Datumsangaben",
        "c": "Für IDs, für Werte die keine feinere Unterteilung brauchen",
        "correct": "c"
    },
    "Welche Datentypen können ge-castet werden? Führen Sie Beispiele dafür an": {
        "a": "CHAR kann niemals zu NUMERIC konvertiert werden",
        "b": "NUMERIC kann nur in TEXT umgewandelt werden",
        "c": "Implizit: SMALLINT -> INTEGER; Explizit: CAST(NUMERIC AS CHAR), CAST(CHAR AS NUMERIC)",
        "correct": "c"
    },
    "Für was verwendet man Constraints bzw. was sind Constraints?": {
        "a": "Constraints sind nur Kommentare in Tabellen",
        "b": "Constraints löschen automatisch doppelte Werte",
        "c": "Constraints definieren Bedingungen für Daten; wenn nicht erfüllt, wird eine Fehlermeldung erzeugt",
        "correct": "c"
    },
    "Was war das Ziel für die Entwicklung von SQL?": {
        "a": "SQL wurde entwickelt, um komplexe mathematische Berechnungen durchzuführen",
        "b": "SQL wurde entwickelt, um auch für Nicht-Programmierer eine einfache Sprache zur Abfrage von Datenbanken bereitzustellen",
        "c": "SQL wurde entwickelt, um nur Textdateien zu verarbeiten",
        "correct": "b"
    },
    "Erklären Sie mind. 3 Anwendungsfälle für SQL": {
        "a": "Nur um Tabellen zu drucken",
        "b": "Nur um Benutzerrechte zu verwalten",
        "c": "Datenbankdefinition, Daten abfragen und filtern, Daten manipulieren",
        "correct": "c"
    },
    "Für was wird DDL (Data Definition Language) verwendet?": {
        "a": "Abfragen von Daten",
        "b": "Manipulation von Datensätzen",
        "c": "Erstellen von Datenbanken, Tabellen und Indizes",
        "correct": "c"
    },
    "Für was wird DQL verwendet?": {
        "a": "Erstellen von Tabellen",
        "b": "Manipulation von Datensätzen",
        "c": "Abfragen von Daten",
        "correct": "c"
    },
    "Für was wird DML (Data Manipulation Language) verwendet?": {
        "a": "Erstellen von Tabellen",
        "b": "Abfragen von Daten",
        "c": "Anlegen, Ändern und Löschen von Datensätzen",
        "correct": "c"
    },
    "Für was wird DCL (Data Control Language) verwendet?": {
        "a": "Nur zum Abfragen von Daten",
        "b": "Nur zur Definition von Tabellen",
        "c": "Anlegen von Benutzern und Vergabe von Zugriffsrechten",
        "correct": "c"
    },
    "Benennen Sie mind. 3 SQL-Befehle im Umgang mit Datenbanken": {
        "a": "INSERT INTO, UPDATE, DELETE",
        "b": "CAST, CONVERT, ALTER",
        "c": "CREATE DATABASE [IF NOT EXISTS] datenbankname; SHOW DATABASES; USE datenbankname; DROP DATABASE [IF EXISTS] datenbankname",
        "correct": "c"
    },
    "Was ist DOM?": {
        "a": "DOM steht für Document Object Model. Es ist eine standardisierte Objektschnittstelle, die mit JavaScript genutzt werden kann",
        "b": "DOM ist ein Datenbankmodell für Dokumente",
        "c": "DOM beschreibt das Design von CSS-Dateien",
        "correct": "a"
    },
    "Was ist das hierarchiehöchste Objekt im DOM? Nennen Sie drei Unterobjekte": {
        "a": "Das höchste Objekt ist document; Unterobjekte sind head, body, title",
        "b": "Das höchste Objekt ist window; Unterobjekte sind frames, document, location",
        "c": "Das höchste Objekt ist HTML; Unterobjekte sind head, body, footer",
        "correct": "b"
    },
    "Wie wird die Struktur eines Dokuments im Browser dargestellt?": {
        "a": "Als Liste von CSS-Klassen",
        "b": "Als Baumstruktur, wobei Elemente als Knoten (nodes) im Speicher abgebildet werden",
        "c": "Als reine Textdatei ohne Struktur",
        "correct": "b"
    },
    "Nennen Sie drei wichtige Knotentypen bei Webseiten": {
        "a": "Dokumentknoten, Elementknoten, Attributknoten",
        "b": "HTML-Knoten, CSS-Knoten, JS-Knoten",
        "c": "Window-Knoten, Frame-Knoten, Script-Knoten",
        "correct": "a"
    },
    "Was bewirkt die DOM-Methode getElementById()?": {
        "a": "Sie gibt ein Array aller Elemente mit einem bestimmten Tag-Namen zurück",
        "b": "Sie selektiert ein HTML-Element anhand seines id-Attributs und liefert den entsprechenden Knoten",
        "c": "Sie ändert den Textinhalt eines Elements",
        "correct": "b"
    },
    "Was bewirkt die DOM-Methode getElementsByTagName()?": {
        "a": "Sie liefert einen Array von Knoten, die den angegebenen Tag-Namen besitzen",
        "b": "Sie selektiert ein einzelnes Element anhand der id",
        "c": "Sie löscht alle Elemente eines bestimmten Typs",
        "correct": "a"
    },
    "Welche drei wesentlichen Kategorien zum Zugriff auf Elemente einer Webseite gibt es?": {
        "a": "Zugriff auf Textinhalte, Zugriff auf Werte von Formularfeldern, Zugriff auf klassische HTML-Attribute",
        "b": "Zugriff auf CSS-Stile, Zugriff auf Browser-Plugins, Zugriff auf Cookies",
        "c": "Zugriff auf Dateien, Zugriff auf Netzwerkdaten, Zugriff auf lokale Speicherung",
        "correct": "a"
    },
    "Wie kann auf Formularinhalte zugegriffen werden?": {
        "a": "Über die CSS-Eigenschaft style",
        "b": "Über die value-Eigenschaft des entsprechenden Elements",
        "c": "Über die id des Formulars ohne weitere Eigenschaften",
        "correct": "b"
    },
    "Für was verwendet man die SELECT-Anweisung?": {
        "a": "Um alle Tabellen einer Datenbank zu löschen",
        "b": "Um aus einer oder mehreren Tabellen genau die Attribute auszuwählen, die für die aktuelle Abfrage gebraucht werden",
        "c": "Um Tabellen zu erstellen",
        "correct": "b"
    },
    "Wie kann man die Ergebnismenge einer SELECT-Anweisung eingrenzen?": {
        "a": "Mit dem Keyword WHERE gefolgt von einem booleschen Ausdruck",
        "b": "Mit der Funktion CAST",
        "c": "Mit dem Befehl INSERT INTO",
        "correct": "a"
    },
    "Welche weiteren optionalen Klauseln wie die WHERE-Klausel kennen Sie? Beschreiben Sie diese kurz": {
        "a": "GROUP BY (Wert), LIMIT (Wert), ORDER BY (Wert) [ASC, DESC]",
        "b": "INSERT, UPDATE, DELETE",
        "c": "CREATE, DROP, ALTER",
        "correct": "a"
    },
    "Wie kann man eine Spaltenüberschrift einer Ergebnismenge ändern? (mit Beispiel)": {
        "a": "Mit dem Keyword AS im SELECT-Statement, z. B.: SELECT vname AS Vorname FROM mitarbeiter",
        "b": "Mit der Funktion SUM()",
        "c": "Mit der ORDER BY-Klausel",
        "correct": "a"
    },
    "Wie kann man im Abfrageergebnis doppelte Datensätze vermeiden?": {
        "a": "Mit der Verwendung von GROUP BY (Wert), um gleiche Werte zu gruppieren und nur einmal anzuzeigen",
        "b": "Mit der WHERE-Klausel",
        "c": "Mit der LIMIT-Klausel",
        "correct": "a"
    },
    "Was ist eine Relation bzw. Was beschreibt sie? Führen Sie drei Eigenschaften an": {
        "a": "Eine Menge von Tupeln (Datensätzen) in der Form einer Tabelle; Eigenschaften: Eindeutiger Name, mehrere Attribute, Primärschlüssel",
        "b": "Eine Liste von Objekten ohne feste Struktur",
        "c": "Eine Sammlung von Werten ohne Beziehung zueinander",
        "correct": "a"
    },
    "Was versteht man unter funktionaler Abhängigkeit?": {
        "a": "Alle Attribute sind unabhängig voneinander",
        "b": "Für einen bestimmten Wert X gibt es immer einen individuellen Wert Y, der sich nicht ändert",
        "c": "Ein Attribut kann beliebige Werte annehmen, unabhängig von anderen",
        "correct": "b"
    },
    "Was versteht man unter transitiver Abhängigkeit?": {
        "a": "Attribute sind in einer Kette zwischen anderen Attributen voneinander abhängig; Beispiel: A von B, B von C → A ist transitiv von C",
        "b": "Alle Attribute hängen nur direkt vom Primärschlüssel ab",
        "c": "Attribute haben keine Abhängigkeiten",
        "correct": "a"
    },
    "Was sind die Ziele der Normalisierung? Mindestens 3": {
        "a": "Verhindert Datenredundanz, verhindert Dateninkonsistenz, sorgt für Sicherheit beim Einfügen/Löschen/Ändern von Datensätzen",
        "b": "Erhöht die Datenredundanz und erlaubt Duplikate",
        "c": "Vereinfachung der Syntax von SQL-Befehlen",
        "correct": "a"
    },
    "Beschreiben Sie die 1:1 Beziehung und führen Sie ein Beispiel an": {
        "a": "Ein Tupel aus einer Relation ist genau einem Tupel aus einer anderen Relation zugeordnet; Beispiel: Postleitzahl und Ort",
        "b": "Ein Tupel kann mehreren Tupeln einer anderen Relation zugeordnet sein",
        "c": "Jede Relation kann beliebig viele Tupel enthalten, ohne Beziehung",
        "correct": "a"
    },
    "Beschreiben Sie die 1:n Beziehung": {
        "a": "Jede Entität einer Entitätsmenge ist genau einem Tupel einer anderen Entität zugeordnet",
        "b": "Jede Entität einer Entitätsmenge kann mehreren Entitäten einer anderen Entitätsmenge zugeordnet sein; Beispiel: Person und Immobilien",
        "c": "Es besteht keine Beziehung zwischen Entitäten",
        "correct": "b"
    },
    "Was ist ein Primärschlüssel?": {
        "a": "Ein eindeutiger Identifikator einer Entität, Wert kommt nur einmal vor",
        "b": "Ein Fremdschlüssel in einer anderen Tabelle",
        "c": "Ein Standardwert für leere Felder",
        "correct": "a"
    },
    "Was ist ein Fremdschlüssel?": {
        "a": "Ein Attribut ohne Bezug zu anderen Tabellen",
        "b": "Der eindeutige Identifikator einer Fremd-Relation, der in der aktuellen Relation eingebunden wird",
        "c": "Ein zufälliger Wert zur Identifikation von Datensätzen",
        "correct": "b"
    },
    "Was versteht man unter NULL-Werten oder leeren Einträgen?": {
        "a": "NULL-Werte zeigen die Absenz von Werten; leere Einträge enthalten einen Standardwert abhängig vom Datentyp",
        "b": "NULL-Werte sind gleich 0; leere Einträge sind leerer Text",
        "c": "NULL-Werte und leere Einträge sind immer gleichwertig und werden automatisch entfernt",
        "correct": "a"
    },
    "Was ist eine Lösch-Anomalie?": {
        "a": "Bei der Löschung eines Datensatzes werden abhängige Datensätze mitgelöscht, was zum Datenverlust führen kann",
        "b": "Beim Löschen eines Datensatzes wird automatisch ein Backup erstellt",
        "c": "Lösch-Anomalien verhindern Datenverlust",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 1. Normalform?": {
        "a": "Wenn jedes Attribut atomar ist und pro Tupel nur ein Eintrag zulässig ist",
        "b": "Wenn jedes Attribut mehrere Werte gleichzeitig enthalten kann",
        "c": "Wenn alle Attribute unabhängig voneinander sind",
        "correct": "a"
    },
    "Wann befindet sich eine Relation in der 2. Normalform?": {
        "a": "Wenn die 1. Normalform erfüllt ist und jedes Nicht-Schlüsselfeld vom Primärschlüssel abhängig ist",
        "b": "Wenn alle Attribute mehrfach vorkommen dürfen",
        "c": "Wenn nur die Primärschlüssel-Attribute existieren",
        "correct": "a"
    },
    "Was ist ein Primärschlüssel und welche Rolle spielt er in einer Tabelle?": {
        "a": "Ein Primärschlüssel ist ein Attribut, das jeden Datensatz eindeutig macht; kann auch aus mehreren Attributen bestehen",
        "b": "Ein Primärschlüssel ist ein Textfeld ohne besondere Bedeutung",
        "c": "Ein Primärschlüssel ist ein Wert, der automatisch für alle Datensätze generiert wird",
        "correct": "a"
    },
    "Welche Vorteile bietet ein Index in einer Datenbank?": {
        "a": "Er verringert die Größe der Datenbank",
        "b": "Durch einen Index kann die Performance beim Abfragen von Daten verbessert werden",
        "c": "Ein Index erstellt automatisch Primärschlüssel",
        "correct": "b"
    },
    "Was ist ein Fremdschlüssel und wie unterstützt er die referenzielle Integrität?": {
        "a": "Er verhindert alle Löschungen in der Datenbank",
        "b": "Ein Fremdschlüssel stellt eine Beziehung zu einem Schlüsselfeld einer anderen Relation her und sorgt für referenzielle Integrität",
        "c": "Ein Fremdschlüssel ist ein Standardwert für leere Felder",
        "correct": "b"
    },
    "Wie kann ein Sekundärschlüssel definiert werden, und worin unterscheidet er sich von einem Primärschlüssel?": {
        "a": "Sekundärschlüssel werden automatisch erstellt",
        "b": "Ein Sekundärschlüssel wird mit UNIQUE definiert und es können mehrere Schlüssel dieser Art existieren",
        "c": "Sekundärschlüssel sind immer Primärschlüssel",
        "correct": "b"
    },
    "Wie erstellt man einen zusammengesetzten Primärschlüssel?": {
        "a": "PRIMARY KEY (Spalte1, Spalte2)",
        "b": "Mit der Funktion COMBINE(Spalte1, Spalte2)",
        "c": "Mit der UNIQUE-Klausel",
        "correct": "a"
    },
    "Welche Nachteile können Indizes mit sich bringen?": {
        "a": "Indizes verringern automatisch die Performance",
        "b": "Zu viele Indizes können die Performance bei INSERT/UPDATE/DELETE verschlechtern und brauchen zusätzlichen Speicherplatz",
        "c": "Indizes verhindern das Einfügen neuer Daten",
        "correct": "b"
    },
    "Was sind typische Einsatzszenarien für Fremdschlüssel in einer Datenbank?": {
        "a": "Nur zur Optimierung von Abfragen",
        "b": "Fremdschlüssel dienen zur Abbildung von Beziehungen und zur Sicherstellung der referenziellen Integrität",
        "c": "Fremdschlüssel werden nur für Textfelder verwendet",
        "correct": "b"
    },
    "Welche Best Practices gibt es beim Erstellen von Indizes?": {
        "a": "Indizes nur für Tabellen mit sehr wenigen Daten erstellen",
        "b": "Indizes nur für häufig verwendete Abfragen erstellen und für Tabellen mit großen Datenmengen",
        "c": "Indizes automatisch für alle Tabellen erstellen",
        "correct": "b"
    }
}
questions4ADAC_INF = {
    "Nenne 3 Beispiele für die Verwendung von den Devtools eines Browsers:": {
        "a": "Nur JavaScript-Code debuggen",
        "b": "HTML-Elemente einsehen/verändern, CSS-Elemente einsehen/verändern, Geräte wie Smartphones/Tablets simulieren",
        "c": "Nur Netzwerkpakete analysieren",
        "correct": "b"
    },
    "Was versteht man unter clientseitiger Programmierung?": {
        "a": "Skripte werden nur auf dem Server ausgeführt",
        "b": "Skripte werden direkt vom Benutzer im Browser ausgeführt, nicht auf dem Server",
        "c": "Skripte laufen ausschließlich in der Cloud",
        "correct": "b"
    },
    "Was ist der Unterschied zwischen einer dynamischen und einer statischen Webseite?": {
        "a": "Eine dynamische Webseite kann Inhalte ändern, eine statische hat feste Inhalte",
        "b": "Eine dynamische Webseite lädt nur Text, eine statische Bilder",
        "c": "Eine statische Webseite wird nur von mobilen Geräten angezeigt",
        "correct": "a"
    },
    "Zwischen welchen Webprogrammierungen unterscheidet man?": {
        "a": "Serverseitige Webprogrammierung: nur für Datenbanken; Clientseitige: nur für Layout",
        "b": "Serverseitige Webprogrammierung: dynamische Inhalte auf Server; Clientseitige Webprogrammierung: Skripte laufen im Browser",
        "c": "Serverseitige Webprogrammierung: nur HTML; Clientseitige: nur CSS",
        "correct": "b"
    },
    "Für was steht CSS und worum kümmert es sich?": {
        "a": "Client Script System; programmiert die Logik der Seite",
        "b": "Content Style Syntax; speichert Inhalte in der Datenbank",
        "c": "Cascading Style Sheet; beschreibt Aussehen, Position und Sichtbarkeit von Elementen",
        "correct": "c"
    },
    "Wozu verwendet man JavaScript?": {
        "a": "Um HTML- und CSS-Eigenschaften dynamisch zu verändern und auf Ereignisse zu reagieren",
        "b": "Um nur Bilder zu speichern",
        "c": "Um statische Inhalte zu schreiben, die sich nie ändern",
        "correct": "a"
    },
    "Auf was hat man mit der DOM-Schnittstelle Zugriff?": {
        "a": "Nur auf CSS-Dateien",
        "b": "Nur auf Netzwerkprotokolle",
        "c": "HTML-Tags, Attribute, Inhalte von HTML-Seiten, XML-Dokumente, SVG-Grafiken",
        "correct": "c"
    },
    "Welche Aufgabe hat ein Web-Browser?": {
        "a": "Er kompiliert HTML-Dateien in ausführbare Programme",
        "b": "Er stellt Webseiten nach W3C-Definition dar und interpretiert HTML, CSS, JavaScript",
        "c": "Er speichert nur lokale Backups von Webseiten",
        "correct": "b"
    },
    "Welche 3 Technologien sind in der clientseitigen Webentwicklung essentiell?": {
        "a": "PHP, MySQL, Ruby",
        "b": "C, C++, Java",
        "c": "HTML, CSS, JavaScript",
        "correct": "c"
    },
    "Welche Gemeinsamkeit teilen sich HTML, CSS und JavaScript?": {
        "a": "Sie werden nur serverseitig ausgeführt",
        "b": "Sie interagieren alle über das DOM (Document Object Model)",
        "c": "Sie benötigen keine Browserunterstützung",
        "correct": "b"
    },
    "Wer verwaltet die Standards für DOM?": {
        "a": "ISO",
        "b": "IEEE",
        "c": "W3C (World Wide Web Consortium)",
        "correct": "c"
    },
    "Was ist Bootstrap und welche Vorteile bietet es?": {
        "a": "Bootstrap ist ein kostenpflichtiges Backend-Framework für Datenbanken",
        "b": "Bootstrap ist ein kostenloses Frontend-Framework mit HTML, CSS und JS-Komponenten, das schnelle, responsive Websites ermöglicht",
        "c": "Bootstrap ist ein Texteditor für HTML-Dateien",
        "correct": "b"
    },
    "Erkläre das Grid-System von Bootstrap": {
        "a": "Ein 12-spaltiges Raster, das Inhalte flexibel anordnet und sich an verschiedene Bildschirmgrößen anpasst",
        "b": "Ein System zur Datenbankanbindung",
        "c": "Ein Server-Framework zur Bereitstellung von Webseiten",
        "correct": "a"
    },
    "Welche Arten von Komponenten bietet Bootstrap?": {
        "a": "Nur Tabellen und Buttons",
        "b": "Typografie, Formulare, Navigation, Tabellen, Buttons, Modalfenster",
        "c": "Nur Backend-Services",
        "correct": "b"
    },
    "Was sind Sass und Less im Zusammenhang mit Bootstrap?": {
        "a": "CSS-Präprozessoren, die Variablen, Mixins und Nesting ermöglichen und Bootstrap effizienter machen",
        "b": "Programmiersprachen für Datenbankabfragen",
        "c": "Grafikdesign-Programme",
        "correct": "a"
    },
    "Wie kann man Bootstrap anpassen?": {
        "a": "Nur durch JavaScript-Plugins",
        "b": "CSS-Overrides, Customizing von Variablen, JavaScript-Plugins",
        "c": "Nur durch Serverkonfiguration",
        "correct": "b"
    },
    "Was sind die Vor- und Nachteile von Bootstrap?": {
        "a": "Schnellere Entwicklung, responsive Design, große Community; Nachteile: weniger Flexibilität, evtl. große CSS-Dateien",
        "b": "Nur Nachteile: sehr kompliziert, keine Dokumentation",
        "c": "Nur Vorteile: läuft automatisch ohne Anpassung",
        "correct": "a"
    },
    "Wie integriert man Bootstrap in ein HTML-Dokument?": {
        "a": "Bootstrap wird über einen CDN-Link im <head>-Bereich eingebunden",
        "b": "Bootstrap muss auf einem Server installiert werden",
        "c": "Bootstrap wird per FTP auf das Gerät heruntergeladen",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen einem Grid-System und einem Flexbox-Layout?": {
        "a": "Grid-System für zweidimensionale Layouts, Flexbox für eindimensionale Layouts",
        "b": "Flexbox ist für Server, Grid nur für Desktop",
        "c": "Es gibt keinen Unterschied",
        "correct": "a"
    },
    "Was ist ein responsive Design und wie wird es mit Bootstrap umgesetzt?": {
        "a": "Ein Layout, das sich automatisch an die Bildschirmgröße anpasst, umgesetzt durch Grid-System und Media Queries",
        "b": "Ein statisches Layout ohne Anpassung",
        "c": "Ein Design nur für Smartphones",
        "correct": "a"
    },
    "Welche anderen Frontend-Frameworks gibt es neben Bootstrap?": {
        "a": "Foundation, Bulma, Materialize, Semantic UI",
        "b": "MySQL, PostgreSQL, MongoDB",
        "c": "Java, Python, C++",
        "correct": "a"
    },
    "Was versteht man unter einem relationalen Datenbanksystem (RDBMS)?": {
        "a": "Ein System, das Daten nur in Dateien speichert",
        "b": "Ein Datenbanksystem, das Daten in Tabellen speichert, die in Beziehungen zueinander stehen und SQL verwendet",
        "c": "Ein System zur Verwaltung von Textdokumenten",
        "correct": "b"
    },
    "Was ist ein Primärschlüssel und welche Aufgabe hat er?": {
        "a": "Ein Attribut oder eine Kombination von Attributen, die jede Zeile eindeutig identifiziert",
        "b": "Ein zufälliges Feld ohne Bedeutung",
        "c": "Ein Attribut, das auf andere Tabellen verweist",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen einem Primärschlüssel und einem Fremdschlüssel?": {
        "a": "Primärschlüssel verweist auf andere Tabellen; Fremdschlüssel identifiziert die Zeilen",
        "b": "Beide sind dasselbe",
        "c": "Primärschlüssel identifiziert jede Zeile eindeutig; Fremdschlüssel verweist auf einen Primärschlüssel einer anderen Tabelle",
        "correct": "c"
    },
    "Wofür verwendet man die SQL-Operation 'Join'?": {
        "a": "Um nur einzelne Zeilen in einer Tabelle zu löschen",
        "b": "Um Tabellen automatisch zu erstellen",
        "c": "Um Daten aus zwei oder mehr Tabellen basierend auf einem gemeinsamen Attribut zu kombinieren",
        "correct": "c"
    },
    "Was ist das Ziel der Normalisierung in einer Datenbank?": {
        "a": "Redundanzen minimieren und Datenintegrität verbessern, indem Daten auf verschiedene Tabellen verteilt werden",
        "b": "Datenbankgröße vergrößern",
        "c": "Alle Daten in einer großen Tabelle speichern",
        "correct": "a"
    },
    "Welche Eigenschaft garantiert die 2. Normalform (2NF)?": {
        "a": "Alle Attribute hängen nur von einem Teil des Schlüssels ab",
        "b": "Nicht-Schlüssel-Attribute hängen vollständig vom gesamten Primärschlüssel ab",
        "c": "Keine Tabellenbeziehungen bestehen",
        "correct": "b"
    },
    "Was ist eine transitive Abhängigkeit, und wie wird sie in der 3. Normalform (3NF) aufgelöst?": {
        "a": "Ein Primärschlüssel hängt von einem Fremdschlüssel ab; 3NF ignoriert dies",
        "b": "Alle Attribute sind unabhängig; 3NF fügt Abhängigkeiten hinzu",
        "c": "Ein Nicht-Schlüssel-Attribut hängt von einem anderen Nicht-Schlüssel-Attribut ab; in 3NF durch Auslagern in separate Tabellen gelöst",
        "correct": "c"
    },
    "Was versteht man unter referenzieller Integrität in einer Datenbank?": {
        "a": "Primärschlüssel müssen NULL-Werte enthalten",
        "b": "Fremdschlüssel müssen auf gültige Primärschlüssel verweisen, um konsistente Beziehungen zu gewährleisten",
        "c": "Tabellen dürfen keine Spalten haben",
        "correct": "b"
    },
    "Erkläre das ACID-Prinzip und wofür es in Datenbanksystemen wichtig ist": {
        "a": "Ein Algorithmus zur Datensicherung auf Servern",
        "b": "Ein Protokoll zur Verschlüsselung von Tabellen",
        "c": "Beschreibt Eigenschaften von Transaktionen: Atomarität, Konsistenz, Isolation, Dauerhaftigkeit",
        "correct": "c"
    },
    "Was ist eine View (Sicht) in einer Datenbank?": {
        "a": "Eine neue physische Tabelle mit doppelten Daten",
        "b": "Ein Backup einer Tabelle",
        "c": "Eine gespeicherte SQL-Abfrage, die als virtuelle Tabelle verwendet wird",
        "correct": "c"
    },
    "Warum wurde JavaScript standardisiert?": {
        "a": "Um die Browserkriege zu beenden und Fragmentierung zu verhindern",
        "b": "Um Java vollständig zu ersetzen",
        "c": "Um JavaScript nur für Desktop-Apps nutzbar zu machen",
        "correct": "a"
    },
    "Welcher Standard definiert JavaScript als herstellerneutrale Sprache?": {
        "a": "HTML5",
        "b": "ECMA-262",
        "c": "ISO-9001",
        "correct": "b"
    },
    "Welche Besonderheit hat var im Vergleich zu let und const?": {
        "a": "Hoisting und Funktions-Scope",
        "b": "Block-Scope",
        "c": "Unveränderbarkeit",
        "correct": "a"
    },
    "Wofür verwendet man const?": {
        "a": "Für Variablen, die mehrfach überschrieben werden können",
        "b": "Für Variablen mit Funktions-Scope",
        "c": "Für eine Konstante, deren Wert nicht neu zugewiesen werden darf",
        "correct": "c"
    },
    "Welches Vererbungsmodell liegt JavaScript zugrunde?": {
        "a": "Prototypische Vererbung",
        "b": "Klassische Vererbung wie in Java",
        "c": "Mehrfachvererbung wie in C++",
        "correct": "a"
    },
    "Welche Syntax erleichtert das Arbeiten mit Objekten, ändert aber den Mechanismus nicht?": {
        "a": "extends",
        "b": "class",
        "c": "function",
        "correct": "b"
    },
    "Welches Problem sollte mit Promises gelöst werden?": {
        "a": "DOM schneller zu laden",
        "b": "Schleifen in JavaScript zu vereinfachen",
        "c": "Callback Hell zu vermeiden",
        "correct": "c"
    },
    "Wie erleichtert async/await die Programmierung?": {
        "a": "Durch vereinfachte Syntax, die wie synchroner Code aussieht",
        "b": "Durch parallele Threads",
        "c": "Durch automatisches Fehler-Logging",
        "correct": "a"
    },
    "Wofür wird Node.js hauptsächlich verwendet?": {
        "a": "Gestaltung von Webseiten",
        "b": "Serverseitige Entwicklung",
        "c": "Datenbankmodellierung",
        "correct": "b"
    },
    "Welches Framework erlaubt die Entwicklung mobiler Apps mit JavaScript?": {
        "a": "Bootstrap",
        "b": "Vue Router",
        "c": "React Native",
        "correct": "c"
    },
    "Was ist ein Event-Listener?": {
        "a": "Ein CSS-Befehl für Hover-Effekte",
        "b": "Ein Code-Snippet, das HTML-Struktur lädt",
        "c": "Eine Funktion, die auf ein Ereignis wartet und darauf reagiert",
        "correct": "c"
    },
    "Welcher Vorteil hat addEventListener gegenüber älteren Methoden?": {
        "a": "Es erlaubt mehrere Listener pro Ereignis",
        "b": "Es ist kürzer zu schreiben",
        "c": "Es ersetzt automatisch removeEventListener",
        "correct": "a"
    },
    "Was nutzt Event Delegation technisch aus?": {
        "a": "CSS-Kaskadierung",
        "b": "Event Bubbling",
        "c": "Promises",
        "correct": "b"
    },
    "Warum ist Event Delegation oft performanter?": {
        "a": "Weil HTML kompakter wird",
        "b": "Weil CSS-Selektoren schneller arbeiten",
        "c": "Weil weniger einzelne Listener im Speicher sind",
        "correct": "c"
    },
    "Wann wird DOMContentLoaded ausgelöst?": {
        "a": "Wenn das HTML-Dokument geladen und der DOM-Baum erstellt ist",
        "b": "Erst wenn alle Bilder und Stylesheets geladen sind",
        "c": "Sobald der erste <script>-Block gelesen ist",
        "correct": "a"
    },
    "Wofür verwendet man window.onload?": {
        "a": "Für Inline-Skripte in HTML",
        "b": "Für Aktionen, die warten müssen, bis alle Ressourcen geladen sind",
        "c": "Für DOM-Manipulation sofort nach Parsen",
        "correct": "b"
    },
    "Was ist die Aufgabe einer JavaScript-Engine wie V8?": {
        "a": "Sie rendert CSS",
        "b": "Sie baut den DOM-Baum auf",
        "c": "Sie führt JavaScript-Code aus",
        "correct": "c"
    },
    "Was ist die Rolle einer Host-Umgebung wie Node.js oder Browser?": {
        "a": "Sie stellt APIs für Interaktion mit der Außenwelt bereit",
        "b": "Sie validiert HTML-Dokumente",
        "c": "Sie optimiert die Laufzeitgeschwindigkeit von CSS",
        "correct": "a"
    },
    "Welche drei Kerntechnologien bilden die Basis des Webs?": {
        "a": "SQL, XML und PHP",
        "b": "Java, Flash und CSS",
        "c": "HTML, CSS und JavaScript",
        "correct": "c"
    },
    "Wie wird in der Universitätsdatenbank die 1:1-Beziehung zwischen Professor und Forschungsbereich sichergestellt?": {
        "a": "Durch einen UNIQUE-Constraint auf die Fremdschlüsselspalte",
        "b": "Durch einen LEFT JOIN zwischen Professoren und Forschungsbereichen",
        "c": "Durch eine zusätzliche Zwischentabelle",
        "correct": "a"
    },
    "Warum handelt es sich bei der Beziehung Professor - Kurse um eine 1:n-Beziehung?": {
        "a": "Weil jeder Kurs von mehreren Professoren gehalten wird",
        "b": "Weil ein Professor mehrere Kurse halten kann, aber jeder Kurs nur genau einen Professor hat",
        "c": "Weil ein Kurs keinem Professor zugeordnet ist",
        "correct": "b"
    },
    "Warum wird bei Studenten und Kursen eine Zwischentabelle benötigt?": {
        "a": "Weil ein Student viele Kurse belegen und ein Kurs von vielen Studenten besucht werden kann",
        "b": "Um Primärschlüssel und Fremdschlüssel zusammenzuführen",
        "c": "Damit Kurse nur einmal pro Semester existieren",
        "correct": "a"
    },
    "Welche Aufgabe hat ein Fremdschlüssel in einer Tabelle?": {
        "a": "Er identifiziert jede Zeile eindeutig",
        "b": "Er verweist auf den Primärschlüssel einer anderen Tabelle und stellt die Beziehung her",
        "c": "Er erzwingt immer eine n:m-Beziehung",
        "correct": "b"
    },
    "Warum wird in der Tabelle Belegung ein kombinierter Primärschlüssel aus StudentID und KursID verwendet?": {
        "a": "Damit ein Student denselben Kurs nicht doppelt belegen kann",
        "b": "Um alle Professoren mit allen Kursen zu verbinden",
        "c": "Damit die Tabelle nur aus Fremdschlüsseln besteht",
        "correct": "a"
    },
    "Welchen DDL-Befehl nutzt man, um einer Tabelle eine neue Spalte hinzuzufügen?": {
        "a": "INSERT INTO",
        "b": "ALTER TABLE ... ADD COLUMN",
        "c": "CREATE VIEW",
        "correct": "b"
    },
    "Mit welchem SQL-Befehl fragt man Daten ab und filtert sie optional?": {
        "a": "SELECT ... WHERE",
        "b": "UPDATE ... SET",
        "c": "JOIN ... ON",
        "correct": "a"
    },
    "Wie verknüpft man Professoren mit Kursen, um Namen und Kurstitel zu erhalten?": {
        "a": "Mit einem LEFT JOIN auf die Tabellen Professoren und Kurse",
        "b": "Mit einem CROSS JOIN",
        "c": "Mit einem INNER JOIN über die ProfID",
        "correct": "c"
    },
    "Wann verwendet man einen LEFT JOIN statt eines INNER JOIN?": {
        "a": "Wenn man auch Datensätze der linken Tabelle sehen möchte, die keine Übereinstimmung in der rechten Tabelle haben",
        "b": "Nur wenn die Fremdschlüssel als UNIQUE definiert sind",
        "c": "Wenn man Datensätze beider Tabellen ohne Bedingung kombinieren möchte",
        "correct": "a"
    },
    "Mit welcher Aggregatsfunktion zählt man alle Studenten in einer Tabelle?": {
        "a": "SUM(StudentID)",
        "b": "AVG(*)",
        "c": "COUNT(*)",
        "correct": "c"
    },
    "Wie zählt man die Kurse pro Professor und filtert nur Professoren mit mehr als einem Kurs?": {
        "a": "Mit GROUP BY ProfID und HAVING COUNT(KursID) > 1",
        "b": "Mit SELECT DISTINCT ProfID",
        "c": "Mit WHERE COUNT(KursID) > 1",
        "correct": "a"
    },
    "Was ist eine VIEW in einer relationalen Datenbank?": {
        "a": "Eine gespeicherte SQL-Abfrage, die wie eine virtuelle Tabelle funktioniert",
        "b": "Eine Kopie aller Tabelleninhalte",
        "c": "Eine Datei auf dem Server",
        "correct": "a"
    },
    "Was bedeutet Referentielle Integrität in einer Datenbank?": {
        "a": "Ein Fremdschlüssel muss auf einen existierenden Primärschlüssel verweisen",
        "b": "Alle Tabellen müssen den gleichen Primärschlüssel haben",
        "c": "Alle Attribute dürfen keine NULL-Werte enthalten",
        "correct": "a"
    },
    "Wie löscht man alle Belegungen zu einem Kurs über eine Subquery?": {
        "a": "DELETE FROM Belegung WHERE KursID = (SELECT KursID FROM Kurse WHERE Titel = 'Datenbanken I')",
        "b": "DROP TABLE Belegung",
        "c": "DELETE * FROM Belegung WHERE Titel = 'Datenbanken I'",
        "correct": "a"
    }
}
questions4ADAC_INF_2 = {
    #Stored Procedures
    "Was sind Stored Procedures?": {
        "a": "Auf dem Server gespeicherte Prozeduren mit SQL-Anweisungen und zusätzlichen Befehlen zur Ablaufsteuerung",
        "b": "Temporäre Abfragen, die nur während einer Sitzung existieren",
        "c": "Clientseitige Skripte zur Datenverarbeitung",
        "correct": "a"
    },
    "Für welches Einsatzgebiet eignen sich Stored Procedures besonders?": {
        "a": "Für einmalige, einfache SELECT-Abfragen",
        "b": "Zur Auslagerung wiederkehrender SQL-Operationen mit abhängigen Inserts in verschiedene Tabellen",
        "c": "Ausschließlich für Backup-Operationen",
        "correct": "b"
    },
    "Welcher Sicherheitsvorteil ergibt sich durch den Einsatz von Stored Procedures?": {
        "a": "Anwender können direkt auf alle Systemtabellen zugreifen",
        "b": "Passwörter werden automatisch verschlüsselt",
        "c": "Anwender können von systemrelevanten Daten abgeschirmt werden, was besseren Datenschutz bietet",
        "correct": "c"
    },
    "Was charakterisiert Select Procedures?": {
        "a": "Sie liefern eine Ergebnismenge und können in SELECT-Abfragen wie eine Tabelle verwendet werden",
        "b": "Sie ändern ausschließlich Datenbestände",
        "c": "Sie geben nur einen Statuscode zurück",
        "correct": "a"
    },
    "Wozu werden Call Procedures verwendet?": {
        "a": "Um Ergebnismengen als Tabelle zurückzugeben",
        "b": "Um Änderungen an Datenbeständen vorzunehmen, wobei normalerweise ein Statuscode über Erfolg oder Misserfolg zurückgegeben wird",
        "c": "Ausschließlich zum Lesen von Daten ohne Veränderungen",
        "correct": "b"
    },
    "Welche zusätzlichen Befehle stehen in Stored Procedures neben SQL-Anweisungen zur Verfügung?": {
        "a": "Nur SELECT und INSERT",
        "b": "Befehle zur Ablaufsteuerung und Auswertung von Bedingungen",
        "c": "Ausschließlich Backup-Befehle",
        "correct": "b"
    },
    "Was ist ein typisches Beispiel für den Einsatz von Stored Procedures?": {
        "a": "Eine einfache SELECT-Abfrage auf eine Tabelle",
        "b": "Ein Prozess mit einer Kette von abhängigen Inserts in unterschiedliche Tabellen",
        "c": "Das Erstellen von Datenbank-Backups",
        "correct": "b"
    },
    "Wo werden Stored Procedures gespeichert?": {
        "a": "Im Browser-Cache des Clients",
        "b": "Auf dem Datenbankserver",
        "c": "In einer externen Konfigurationsdatei",
        "correct": "b"
    },
    # Trigger
    "Was ist ein Trigger?": {
        "a": "Eine vom Anwender manuell gestartete Stored Procedure",
        "b": "Eine besondere Form der Stored Procedures, die durch das Datenbanksystem selbst bei definierten Ereignissen gestartet wird",
        "c": "Ein Backup-Mechanismus für Datenbanken",
        "correct": "b"
    },
    "Auf welche Ereignisse kann ein Trigger innerhalb einer Tabelle reagieren?": {
        "a": "Nur auf INSERT",
        "b": "Nur auf DELETE",
        "c": "Auf INSERT, UPDATE und DELETE",
        "correct": "c"
    },
    "Welche Bestandteile gehören zu einem Trigger?": {
        "a": "Name, Bedingung für Aktivierung und Ausführungsteil",
        "b": "Nur der Name und die Bedingung",
        "c": "Nur der Ausführungsteil",
        "correct": "a"
    },
    "Kann ein Trigger mehrere Tabellen gleichzeitig überwachen?": {
        "a": "Ja, ein Trigger kann beliebig viele Tabellen überwachen",
        "b": "Nein, ein Trigger bezieht sich stets auf eine bestimmte Tabelle oder Sicht",
        "c": "Ja, aber nur maximal zwei Tabellen",
        "correct": "b"
    },
    "Was ermöglichen die Transitionsvariablen NEW und OLD?": {
        "a": "Den Zugriff auf Werte einer Variable vor bzw. nach der definierten Aktion",
        "b": "Das Löschen alter Datensätze",
        "c": "Das Erstellen neuer Tabellen",
        "correct": "a"
    },
    "Was bewirkt die Angabe von FOR EACH ROW bei einem Trigger?": {
        "a": "Der Trigger wird nur einmal auf die gesamte Tabelle angewendet",
        "b": "Der Trigger wird für jeden einzelnen Datensatz ausgeführt, der von der Anweisung betroffen ist",
        "c": "Der Trigger wird nur auf die erste Zeile angewendet",
        "correct": "b"
    },
    "Wie wird ein Trigger gestartet?": {
        "a": "Manuell durch den Datenbankadministrator",
        "b": "Automatisch durch das Datenbanksystem bei definierten Ereignissen",
        "c": "Durch eine separate Anwendung außerhalb der Datenbank",
        "correct": "b"
    },
    "Worauf bezieht sich ein Trigger immer?": {
        "a": "Auf mehrere verschiedene Tabellen gleichzeitig",
        "b": "Auf die gesamte Datenbank",
        "c": "Auf eine bestimmte Tabelle oder eine bestimmte Sicht",
        "correct": "c"
    },
    "Was ist ein typischer Anwendungsfall für Transitionsvariablen wie NEW.id?": {
        "a": "Zugriff auf den Wert des Feldes 'id' nach der Aktion",
        "b": "Löschen der Spalte 'id'",
        "c": "Erstellen einer neuen Tabelle namens 'id'",
        "correct": "a"
    },
    # Caching
    "Was ist Caching?": {
        "a": "Eine Technik zum dauerhaften Speichern von Daten auf der Festplatte",
        "b": "Eine Technik, bei der Kopien häufig abgerufener Daten an einem schnellen Speicherort abgelegt werden",
        "c": "Ein Verfahren zum Verschlüsseln von Datenbankinhalten",
        "correct": "b"
    },
    "Welche drei Hauptvorteile bietet Caching?": {
        "a": "Geschwindigkeit, Effizienz und Verfügbarkeit",
        "b": "Sicherheit, Verschlüsselung und Komprimierung",
        "c": "Backup, Recovery und Archivierung",
        "correct": "a"
    },
    "Wie funktioniert ein Browser-Cache?": {
        "a": "Er lädt alle Daten bei jedem Besuch neu aus dem Internet",
        "b": "Er speichert bestimmte Teile einer Webseite auf der Festplatte des Nutzers, sodass sie beim erneuten Besuch nicht neu geladen werden müssen",
        "c": "Er komprimiert Webseiten automatisch",
        "correct": "b"
    },
    "Was ist ein Content Delivery Network (CDN)?": {
        "a": "Ein zentraler Server, der alle Webinhalte speichert",
        "b": "Ein weltweit verteiltes Netzwerk von Servern, das statische Inhalte von geografisch nahen Standorten liefert",
        "c": "Eine Datenbank für dynamische Inhalte",
        "correct": "b"
    },
    "Was versteht man unter einem In-Memory-Cache?": {
        "a": "Daten werden auf der Festplatte gespeichert",
        "b": "Daten werden direkt im Arbeitsspeicher (RAM) gehalten, z.B. mit Redis oder Memcached",
        "c": "Daten werden in der Cloud gespeichert",
        "correct": "b"
    },
    "Was ist die größte Herausforderung beim Caching?": {
        "a": "Die Geschwindigkeit des Caches",
        "b": "Die Cache-Invalidierung, also zu wissen, wann zwischengespeicherte Daten veraltet sind",
        "c": "Die Größe des Caches",
        "correct": "b"
    },
    "Was ist eine Time-To-Live (TTL) Strategie?": {
        "a": "Eine Strategie, bei der festgelegt wird, wie lange Daten im Cache gültig sind, bevor sie automatisch entfernt werden",
        "b": "Eine Methode zum dauerhaften Speichern von Daten",
        "c": "Ein Verfahren zur Datenkomprimierung",
        "correct": "a"
    },
    "Was ist ein Cache Hit?": {
        "a": "Die angefragte Information ist nicht im Cache vorhanden",
        "b": "Die angefragte Information wird im Cache gefunden und schnell geliefert",
        "c": "Der Cache ist voll und muss geleert werden",
        "correct": "b"
    },
    "Was ist ein Cache Miss?": {
        "a": "Die Daten werden erfolgreich aus dem Cache geladen",
        "b": "Die Daten sind nicht im Cache und müssen vom langsameren Ursprungsort geholt werden",
        "c": "Der Cache funktioniert nicht mehr",
        "correct": "b"
    },
    "Welche Arten von Inhalten werden typischerweise in einem CDN gespeichert?": {
        "a": "Nur Textdateien",
        "b": "Statische Inhalte wie Bilder, Videos, CSS-Dateien und JavaScript",
        "c": "Ausschließlich Datenbankinhalte",
        "correct": "b"
    },
    "Was speichert ein Datenbank-Cache?": {
        "a": "Alle Tabellen der Datenbank dauerhaft",
        "b": "Die Ergebnisse von häufig ausgeführten Datenbankabfragen",
        "c": "Nur Passwörter und Zugangsdaten",
        "correct": "b"
    },
    "Was charakterisiert einen Objekt-Cache?": {
        "a": "Er speichert nur primitive Datentypen",
        "b": "Er speichert ganze Objekte oder aufwendig berechnete Datenstrukturen",
        "c": "Er funktioniert nur mit JSON-Daten",
        "correct": "b"
    },
    "Warum verbessert Caching die Effizienz?": {
        "a": "Es erhöht die Datenbankgröße",
        "b": "Es reduziert die Last auf ursprünglichen Datenspeichern und spart Rechenleistung und Kosten",
        "c": "Es erstellt automatisch Backups",
        "correct": "b"
    },
    "Wie trägt Caching zur Verfügbarkeit bei?": {
        "a": "Es verhindert alle Systemausfälle vollständig",
        "b": "Wenn das Ursprungssystem ausfällt, kann der Cache manchmal weiterhin Daten liefern",
        "c": "Es erstellt automatisch redundante Server",
        "correct": "b"
    },
    # Sessions
    "Warum sind Sessions in der Webentwicklung notwendig?": {
        "a": "Weil HTTP ein zustandsloses Protokoll ist und Sessions ermöglichen, Benutzer über mehrere Seitenaufrufe zu identifizieren",
        "b": "Um die Internetgeschwindigkeit zu erhöhen",
        "c": "Um die Datenbank zu entlasten",
        "correct": "a"
    },
    "Wie identifiziert ein Server eine bestimmte Benutzersitzung?": {
        "a": "Durch die IP-Adresse des Benutzers",
        "b": "Durch eine zufällige, eindeutige 32-stellige Session-ID, die bei jedem Seitenaufruf gesendet wird",
        "c": "Durch den Browser-Namen",
        "correct": "b"
    },
    "Wo muss die Funktion session_start() platziert werden?": {
        "a": "Am Ende der PHP-Datei",
        "b": "Ganz am Anfang einer PHP-Datei, noch bevor irgendeine Ausgabe an den Browser gesendet wird",
        "c": "Irgendwo in der Mitte der Datei",
        "correct": "b"
    },
    "Wie werden Daten in einer Session gespeichert?": {
        "a": "Über die Variable $_POST",
        "b": "Über die superglobale Array-Variable $_SESSION",
        "c": "Über normale lokale Variablen",
        "correct": "b"
    },
    "Wo werden Session-Daten physisch gespeichert?": {
        "a": "Im Browser des Benutzers",
        "b": "In einer Textdatei auf dem Webserver, typischerweise im Ordner für temporäre Dateien",
        "c": "In der Datenbank",
        "correct": "b"
    },
    "Was ist die Standarddauer einer Session bei Inaktivität?": {
        "a": "60 Sekunden",
        "b": "1440 Sekunden (24 Minuten)",
        "c": "Eine Stunde",
        "correct": "b"
    },
    "Wie löscht man eine einzelne Variable aus einer Session?": {
        "a": "Mit der Funktion unset(), z.B. unset($_SESSION['vorname'])",
        "b": "Mit der Funktion delete()",
        "c": "Mit session_destroy()",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen $_SESSION = array(); und session_destroy()?": {
        "a": "Es gibt keinen Unterschied",
        "b": "$_SESSION = array(); leert alle Session-Variablen, aber die Session läuft weiter; session_destroy() beendet die komplette Session",
        "c": "Beide Befehle machen genau das Gleiche",
        "correct": "b"
    },
    "Was passiert, wenn ein Benutzer Cookies im Browser deaktiviert hat?": {
        "a": "Sessions funktionieren normal weiter",
        "b": "Sessions funktionieren nicht korrekt, da die Session-ID nicht gespeichert werden kann",
        "c": "Die Webseite lädt schneller",
        "correct": "b"
    },
    "Wann endet eine Session?": {
        "a": "Nur wenn der Computer ausgeschaltet wird",
        "b": "Wenn der Benutzer den Browser schließt, session_destroy() aufgerufen wird oder ein Timeout verstreicht",
        "c": "Sessions enden nie automatisch",
        "correct": "b"
    },
    "Welche PHP-Funktion beendet eine komplette Session?": {
        "a": "unset($_SESSION)",
        "b": "session_end()",
        "c": "session_destroy()",
        "correct": "c"
    },
    "Was wird in einem Cookie gespeichert, um Sessions zu ermöglichen?": {
        "a": "Alle Session-Daten des Benutzers",
        "b": "Die Session-ID",
        "c": "Das Passwort des Benutzers",
        "correct": "b"
    },
    "Was passiert mit dem Timeout bei jedem neuen Seitenaufruf während einer Session?": {
        "a": "Der Timeout wird kürzer",
        "b": "Die Zeitspanne wird zurückgesetzt",
        "c": "Der Timeout bleibt unverändert",
        "correct": "b"
    },
    "Wie lang ist eine typische Session-ID?": {
        "a": "8 Zeichen",
        "b": "16 Zeichen",
        "c": "32 Zeichen",
        "correct": "c"
    },
    "Was würde $_SESSION['benutzer'] = 'Maxi'; bewirken?": {
        "a": "Es löscht den Benutzer 'Maxi'",
        "b": "Es speichert den Wert 'Maxi' unter dem Schlüssel 'benutzer' in der Session",
        "c": "Es beendet die Session",
        "correct": "b"
    },
    # AJAX
    "Was bedeutet AJAX und wofür steht die Abkürzung?": {
        "a": "Advanced Java And XML",
        "b": "Asynchronous JavaScript and XML - eine Technik zum Datenaustausch ohne Neuladen der Seite",
        "c": "Automated JavaScript Ajax eXecution",
        "correct": "b"
    },
    "Was ist das XMLHttpRequest-Objekt und wofür wird es verwendet?": {
        "a": "Ein Tool zum Erstellen von XML-Dokumenten",
        "b": "Eine Datenbank für Browser-Daten",
        "c": "Das Herzstück von AJAX, um HTTP-Anfragen zu senden und Antworten zu empfangen ohne Seitenneuladung",
        "correct": "c"
    },
    "Wie wird eine HTTP-Anfrage mit dem XMLHttpRequest-Objekt initialisiert?": {
        "a": "Mit der Methode send()",
        "b": "Mit der Methode start()",
        "c": "Mit der Methode open(), wobei HTTP-Methode, URL und Asynchronität übergeben werden",
        "correct": "c"
    },
    "Was ist der Unterschied zwischen GET und POST im Kontext von AJAX?": {
        "a": "GET ist schneller, POST ist langsamer",
        "b": "GET funktioniert nur mit XML, POST nur mit JSON",
        "c": "GET hängt Parameter an die URL an (kleinere Daten), POST überträgt Daten im Nachrichtenrumpf (größere/sensible Daten)",
        "correct": "c"
    },
    "Was ist die Same-Origin-Policy?": {
        "a": "Eine Regel, die vorschreibt, dass alle Daten verschlüsselt werden müssen",
        "b": "Eine Richtlinie zum Komprimieren von Daten",
        "c": "Eine Sicherheitsrichtlinie, die verhindert, dass AJAX-Anfragen an andere Domains gesendet werden, um XSS zu vermeiden",
        "correct": "c"
    },
    "Welche Funktion hat der Eventhandler onreadystatechange?": {
        "a": "Er initialisiert die AJAX-Anfrage",
        "b": "Er beendet die Verbindung zum Server",
        "c": "Er wird bei jeder Zustandsänderung der AJAX-Anfrage aufgerufen, hauptsächlich um den Abschluss zu prüfen",
        "correct": "c"
    },
    "Was bedeutet readyState = 4?": {
        "a": "Verbindung wird aufgebaut",
        "b": "Antwort wird empfangen",
        "c": "Anfrage abgeschlossen und Antwort bereit",
        "correct": "c"
    },
    "Was bedeutet readyState = 0?": {
        "a": "Anfrage nicht initialisiert",
        "b": "Verbindung aufgebaut",
        "c": "Anfrage gesendet",
        "correct": "a"
    },
    "Was ist der Unterschied zwischen responseText und responseXML?": {
        "a": "responseText ist schneller als responseXML",
        "b": "Es gibt keinen Unterschied",
        "c": "responseText liefert die Antwort als Zeichenkette, responseXML als XML-Dokument/DOM-Struktur",
        "correct": "c"
    },
    "Welche Vorteile bietet JSON im Vergleich zu XML in AJAX?": {
        "a": "JSON ist komplexer und ausdrucksstärker",
        "b": "JSON funktioniert nur mit POST-Anfragen",
        "c": "JSON ist schlanker, einfacher zu verarbeiten, nativ in JavaScript unterstützt und benötigt weniger Speicher",
        "correct": "c"
    },
    "Wie werden Daten per AJAX über POST an den Server gesendet?": {
        "a": "Mit der Methode open() und automatischer Übertragung",
        "b": "Nur durch Anhängen an die URL",
        "c": "Mit der Methode send() und setRequestHeader() zum Setzen des Content-Types wie 'application/x-www-form-urlencoded'",
        "correct": "c"
    },
    "Was bedeutet readyState = 2?": {
        "a": "Verbindung aufgebaut",
        "b": "Anfrage gesendet",
        "c": "Antwort wird empfangen",
        "correct": "b"
    },
    "Warum ist AJAX wichtig für moderne Webanwendungen?": {
        "a": "Es macht Webseiten bunter",
        "b": "Es erhöht die Serverlast",
        "c": "Es ermöglicht Datenaustausch ohne Neuladen der Seite, was die Benutzererfahrung verbessert",
        "correct": "c"
    },
    "Was muss bei POST-Anfragen mit setRequestHeader() gesetzt werden?": {
        "a": "Die Dateigröße",
        "b": "Die Serveradresse",
        "c": "Der Content-Type, z.B. 'application/x-www-form-urlencoded'",
        "correct": "c"
    },
    "Was bedeutet readyState = 3?": {
        "a": "Anfrage nicht initialisiert",
        "b": "Anfrage gesendet",
        "c": "Antwort wird empfangen",
        "correct": "c"
    }
}






