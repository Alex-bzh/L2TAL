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
                <title>Présentation | <xsl:apply-templates select="show/@title"/></title>
                <meta charset="utf-8"/>
            </head>
            <body>
                <!-- call for application for attribute 'title', child of element 'show' -->
                <h1><xsl:apply-templates select="show/@title"/></h1>
                <p>
                    <b>Créateurs :</b>
                    <xsl:text> </xsl:text>
                    <!-- call for nodes 'author' -->
                    <xsl:apply-templates select="//author"/>
                    <br/>
                    <b>Année de création :</b>
                    <xsl:text> </xsl:text>
                    <!-- call for nodes 'year' (only one) -->
                    <xsl:apply-templates select="//year"/>
                </p>
            </body>
        </html>

    </xsl:template>
    
    <!-- a template than can apply to all calls -->
    <xsl:template match="*">
        <!-- copy the textual content of the current node -->
        <xsl:value-of select="."/>
    </xsl:template>

    <!-- candidate 'author' -->
    <xsl:template match="author">
        <!-- copy the textual content of the current node -->
        <xsl:value-of select="."/>
        <!-- if the current node is not the last one, add a comma -->
        <xsl:if test="position() != last()">, </xsl:if>
    </xsl:template>

</xsl:stylesheet>