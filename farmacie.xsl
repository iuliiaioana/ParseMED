<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Medicamente</h2>
                <table border="2">
                    <tr bgcolor="#9acd32">
                        <th>Nume</th>
                        <th>Afectiuni</th>
                        <th>Cod Producator</th>
                        <th>Producator</th>
                        <th>Mod Administrare</th>
                        <th>Substanta activa</th>
                        <th>Reactii adverse</th>
                        <th>Pret</th>
                    </tr>
                    <xsl:for-each select="farmacie/medicament">
                        <tr>
                            <td>
                                <xsl:value-of select="nume" />
                            </td>
                            <td>
                                <xsl:for-each select="afectiune_medicala">
                                    <xsl:value-of select="." />
                                    <br></br>
                                </xsl:for-each>
                            </td>
                            <td>
                                #<xsl:value-of select="producator/@cod" />
                            </td>
                            <td>
                                <xsl:value-of select="producator" />
                            </td>
                            <td>
                                <xsl:value-of select="prospect/mod_administrare" />
                            </td>
                            <td>
                                <xsl:for-each select="prospect/substanta_activa">
                                    <xsl:value-of select="." />(<xsl:value-of select="./@gramaj" />),
                                    <br></br>
                                </xsl:for-each>
                            </td>
                            <td>
                                <xsl:value-of select="prospect/reactie_adversa" />
                            </td>
                            <td>
                                <xsl:value-of select="pret" />
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>