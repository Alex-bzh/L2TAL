<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" version="1.0" encoding="utf-8" indent="yes"/>
    <!-- main template (backbone) -->
    <xsl:template match="/">
        <bbt>
            <xsl:apply-templates select="//author"/>
            <xsl:apply-templates select="//year"/>
        </bbt>
    </xsl:template>
    <!-- candidates -->
    <xsl:template match="author">
        <createur>
            <xsl:value-of select="."/>
        </createur>
    </xsl:template>
    <xsl:template match="year">
        <annee>
            <xsl:value-of select="."/>
        </annee>
    </xsl:template>
</xsl:stylesheet>