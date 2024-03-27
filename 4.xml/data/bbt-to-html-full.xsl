<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- an HTML document will be produced -->
    <xsl:output method="html" encoding="utf-8" indent="yes"/>

    <!-- backbone -->
    <xsl:template match="/">

        <xsl:text disable-output-escaping="yes">&amp;lt;!DOCTYPE html&amp;gt;</xsl:text>
        <xsl:text>&amp;#xA;</xsl:text>

        <html lang="fr" xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title><xsl:value-of select="/show/meta/title"/></title>
                <meta charset="utf-8"/>
            </head>
            <body>
                <h1><xsl:value-of select="/show/meta/title"/></h1>
                <p><xsl:apply-templates select="/show/meta/summary[@xml:lang='fr']"/></p>
                <h2>Les personnages</h2>
                <ul>
                    <xsl:apply-templates select="//character"/>
                </ul>
            </body>
        </html>

    </xsl:template>

    <!-- candidate 'character' -->
    <xsl:template match="character">
        <xsl:variable name="id" select="@id" />
        <li>
            <xsl:value-of select="firstName"/>
            <xsl:if test="lastName">
                <xsl:text> </xsl:text>
                <xsl:value-of select="lastName"/>
            </xsl:if>
            <xsl:apply-templates select="//actor[@ref = $id]"/>
        </li>
    </xsl:template>
    
    <!-- candidate 'actor' -->
    <xsl:template match="actor">
        <xsl:value-of select="concat(' (', firstName, ' ', lastName, ')')"/>
    </xsl:template>

</xsl:stylesheet>