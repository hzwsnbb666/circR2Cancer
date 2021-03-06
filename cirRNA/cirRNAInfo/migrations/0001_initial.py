# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-07 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cancer_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100, null=True, verbose_name='disease')),
                ('DOID', models.CharField(max_length=500, null=True, verbose_name='DOID')),
                ('Definition', models.CharField(max_length=500, null=True, verbose_name='DOID')),
                ('Xrefs', models.CharField(max_length=500, null=True, verbose_name='Xrefs')),
                ('Subsets', models.CharField(max_length=500, null=True, verbose_name='Subsets')),
                ('Synonyms', models.CharField(max_length=500, null=True, verbose_name='Synoyms')),
                ('Relationships', models.CharField(max_length=500, null=True, verbose_name='Relationships')),
            ],
        ),
        migrations.CreateModel(
            name='circRNA_cancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circRNA', models.CharField(max_length=100, null=True, verbose_name='circRNA')),
                ('disease', models.CharField(max_length=100, null=True, verbose_name='disease')),
                ('method_of_circRNA_direction', models.CharField(max_length=100, null=True, verbose_name='method_of_circRNA_direction')),
                ('expression_pattern', models.CharField(max_length=100, null=True, verbose_name='expression_pattern')),
                ('Chromosome', models.CharField(max_length=100, null=True, verbose_name='Chromosome')),
                ('Region', models.CharField(max_length=100, null=True, verbose_name='Region')),
                ('Strand', models.CharField(max_length=100, null=True, verbose_name='strand')),
                ('Gene_Symbol', models.CharField(max_length=100, null=True, verbose_name='Gene_Symbol')),
                ('host_gene', models.CharField(max_length=100, null=True, verbose_name='host_gene')),
                ('tissue_or_cell_line', models.CharField(max_length=100, null=True, verbose_name='tissue_or_cell_line')),
                ('Transcription_interval', models.CharField(max_length=100, null=True, verbose_name='Transcription_interval')),
                ('species', models.CharField(max_length=100, null=True, verbose_name='species')),
                ('pmid', models.CharField(max_length=100, null=True, verbose_name='pmid')),
                ('functional_describution', models.CharField(max_length=500, null=True, verbose_name='functional_describution')),
                ('sequence', models.CharField(max_length=500, null=True, verbose_name='sequence')),
            ],
        ),
        migrations.CreateModel(
            name='circrna_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circRNA', models.CharField(max_length=500, null=True, verbose_name='circRNA')),
                ('method_of_circRNA_direction', models.CharField(max_length=500, null=True, verbose_name='method_of_circRNA_direction')),
                ('expression_pattern', models.CharField(max_length=100, null=True, verbose_name='expression_pattern')),
                ('Chromosome', models.CharField(max_length=100, null=True, verbose_name='Chromosome')),
                ('Region', models.CharField(max_length=100, null=True, verbose_name='Region')),
                ('Strand', models.CharField(max_length=100, null=True, verbose_name='Strand')),
                ('Gene_Symbol', models.CharField(max_length=100, null=True, verbose_name='Gene_Sym')),
                ('host_gene', models.CharField(max_length=100, null=True, verbose_name='host_gene')),
                ('tissue_or_cell_line', models.CharField(max_length=100, null=True, verbose_name='tissue_cell')),
                ('Transcription_interval', models.CharField(max_length=200, null=True, verbose_name='Transcription_interval')),
                ('Sequence', models.CharField(max_length=500, null=True, verbose_name='Sequence')),
            ],
        ),
        migrations.CreateModel(
            name='circRNA_miRNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circRNA', models.CharField(max_length=100, null=True, verbose_name='circRNA')),
                ('miRNA', models.CharField(max_length=100, null=True, verbose_name='miRNA')),
            ],
        ),
        migrations.CreateModel(
            name='cirrna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cirrna', models.CharField(max_length=500, null=True, verbose_name='name_cirrna')),
                ('chrom', models.CharField(max_length=500, null=True, verbose_name='chrom')),
                ('start', models.CharField(max_length=500, null=True, verbose_name='start')),
                ('end', models.CharField(max_length=500, null=True, verbose_name='end')),
                ('strand', models.CharField(max_length=500, null=True, verbose_name='strand')),
                ('circRNA_ID', models.CharField(max_length=500, null=True, verbose_name='circRNA ID')),
                ('genomic_length', models.CharField(max_length=500, null=True, verbose_name='genomic length')),
                ('spliced_seq_length', models.CharField(max_length=500, null=True, verbose_name='spliced seq length')),
                ('samples', models.CharField(max_length=500, null=True, verbose_name='samples')),
                ('repeats', models.CharField(max_length=500, null=True, verbose_name='repeats')),
                ('annotation', models.CharField(max_length=500, null=True, verbose_name='annotation')),
                ('best_transcript', models.CharField(max_length=500, null=True, verbose_name='best transcript')),
                ('gene_symbol', models.CharField(max_length=500, null=True, verbose_name='gene symbol')),
                ('circRNA_study', models.CharField(max_length=500, null=True, verbose_name='circRNA study')),
            ],
        ),
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_incirrna', models.CharField(max_length=500, null=True, verbose_name='name in cirRNA')),
                ('name', models.CharField(max_length=500, null=True, verbose_name='name')),
                ('DOID', models.TextField(null=True, verbose_name='id')),
                ('Definition', models.TextField(null=True, verbose_name='def')),
                ('Xrefs', models.TextField(null=True, verbose_name='xref')),
                ('Alternateids', models.TextField(null=True, verbose_name='alt_id')),
                ('Subsets', models.TextField(null=True, verbose_name='subset')),
                ('Synonyms', models.TextField(null=True, verbose_name='synonym')),
                ('Relationships', models.TextField(null=True, verbose_name='is_a')),
            ],
        ),
        migrations.CreateModel(
            name='miRNA_cancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miRNA', models.CharField(max_length=100, null=True, verbose_name='circRNA')),
                ('disease', models.CharField(max_length=100, null=True, verbose_name='disease')),
                ('pmid', models.CharField(max_length=100, null=True, verbose_name='pmid')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='miRNA_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miRNA', models.CharField(max_length=100, null=True, verbose_name='circRNA')),
                ('Accession', models.CharField(max_length=100, null=True, verbose_name='Accession')),
                ('symbol', models.CharField(max_length=100, null=True, verbose_name='symbol')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='description')),
                ('gene_family', models.CharField(max_length=100, null=True, verbose_name='gene_family')),
                ('Genome_context', models.CharField(max_length=500, null=True, verbose_name='Genome_context')),
                ('Clustered_miRNAs', models.CharField(max_length=500, null=True, verbose_name='Clustered_miRNAs')),
                ('database_links', models.CharField(max_length=500, null=True, verbose_name='database_links')),
            ],
        ),
        migrations.CreateModel(
            name='relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cir_bace_id', models.CharField(max_length=100, null=True, verbose_name='cir_bace_id')),
                ('cir_id', models.CharField(max_length=500, null=True, verbose_name='cir_id')),
                ('displaycir_id', models.CharField(max_length=500, null=True, verbose_name='displaycir_id')),
                ('disease_name', models.CharField(max_length=500, null=True, verbose_name='disease_name')),
                ('pmid', models.CharField(max_length=500, null=True, verbose_name='pmid')),
                ('evidence', models.CharField(max_length=5000, null=True, verbose_name='evidence')),
            ],
        ),
    ]
