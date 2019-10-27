from django.db import models

# Create your models here.

class disease(models.Model):
    """
    疾病信息
    """
    name_incirrna = models.CharField('name in cirRNA', max_length=500, null=True)

    name = models.CharField('name', max_length=500, null=True)

    DOID = models.TextField('id',  null=True)

    Definition =  models.TextField('def',  null=True)

    Xrefs =  models.TextField('xref', null=True)

    Alternateids  =  models.TextField('alt_id', null=True)

    Subsets   =  models.TextField('subset', null=True)

    Synonyms  =  models.TextField('synonym',null=True)

    Relationships  =  models.TextField('is_a', null=True)

    def __str__(self):
        return self.name_incirrna



class cirrna(models.Model):
    """
    cirRNA信息
    """
    name_cirrna = models.CharField('name_cirrna', max_length=500, null=True)

    chrom = models.CharField('chrom', max_length=500, null=True)

    start = models.CharField('start', max_length=500, null=True)

    end =  models.CharField('end', max_length=500, null=True)

    strand =  models.CharField('strand', max_length=500,null=True)

    circRNA_ID  =  models.CharField('circRNA ID',max_length=500, null=True)

    genomic_length   =  models.CharField('genomic length', max_length=500,null=True)

    spliced_seq_length  =  models.CharField('spliced seq length',max_length=500,null=True)

    samples  =  models.CharField('samples', max_length=500,null=True)


    repeats = models.CharField('repeats', max_length=500, null=True)

    annotation = models.CharField('annotation', max_length=500,null=True)

    best_transcript = models.CharField('best transcript', max_length=500, null=True)

    gene_symbol = models.CharField('gene symbol', max_length=500, null=True)

    circRNA_study = models.CharField('circRNA study', max_length=500, null=True)
    

    def __str__(self):
        return self.name_cirrna




class relationship(models.Model):
    """
    cirRNA信息
    """
    cir_bace_id = models.CharField('cir_bace_id', max_length=100, null=True)

    cir_id = models.CharField('cir_id', max_length=500, null=True)

    displaycir_id = models.CharField('displaycir_id', max_length=500, null=True)

    disease_name = models.CharField('disease_name', max_length=500, null=True)

    pmid =  models.CharField('pmid', max_length=500, null=True)

    evidence =  models.CharField('evidence', max_length=5000,null=True)

   
    

    def __str__(self):
        return self.displaycir_id

class circRNA_miRNA(models.Model):
    circRNA = models.CharField("circRNA",max_length=100,null=True)
    miRNA = models.CharField("miRNA",max_length=100,null=True)
class cancer_info(models.Model):
    disease=models.CharField("disease",max_length=100,null=True)
    DOID=models.CharField("DOID",max_length=500,null=True)
    Definition=models.CharField("DOID",max_length=500,null=True)
    Xrefs=models.CharField("Xrefs",max_length=500,null=True)
    Subsets=models.CharField("Subsets",max_length=500,null=True)
    Synonyms=models.CharField("Synoyms",max_length=500,null=True)
    Relationships=models.CharField("Relationships",max_length=500,null=True)
class circRNA_cancer(models.Model):
    circRNA=models.CharField("circRNA",max_length=100,null=True)
    disease=models.CharField("disease",max_length=100,null=True)
    method_of_circRNA_direction=models.CharField("method_of_circRNA_direction",max_length=100,null=True)
    expression_pattern=models.CharField("expression_pattern",max_length=100,null=True)
    Chromosome=models.CharField("Chromosome",max_length=100,null=True)
    Region=models.CharField("Region",max_length=100,null=True)
    Strand=models.CharField("strand",max_length=100,null=True)
    Gene_Symbol=models.CharField("Gene_Symbol",max_length=100,null=True)
    host_gene=models.CharField("host_gene",max_length=100,null=True)
    tissue_or_cell_line=models.CharField("tissue_or_cell_line",max_length=100,null=True)
    Transcription_interval=models.CharField("Transcription_interval",max_length=100,null=True)
    species=models.CharField("species",max_length=100,null=True)
    pmid=models.CharField("pmid",max_length=100,null=True)
    functional_describution=models.CharField("functional_describution",max_length=500,null=True)
    sequence=models.CharField("sequence",max_length=500,null=True)
class miRNA_cancer(models.Model):
    miRNA=models.CharField("circRNA",max_length=100,null=True)
    disease = models.CharField("disease", max_length=100, null=True)
    pmid=models.CharField("pmid",max_length=100,null=True)
    description=models.CharField("description",max_length=500,null=True)
class miRNA_info(models.Model):
    miRNA=models.CharField("circRNA",max_length=100,null=True)
    Accession=models.CharField("Accession",max_length=100,null=True)
    symbol=models.CharField("symbol",max_length=100,null=True)
    description=models.CharField("description",max_length=500,null=True)
    gene_family=models.CharField("gene_family",max_length=100,null=True)
    Genome_context=models.CharField("Genome_context",max_length=500,null=True)
    Clustered_miRNAs=models.CharField("Clustered_miRNAs",max_length=500,null=True)
    database_links=models.CharField("database_links",max_length=500,null=True)
class circrna_info(models.Model):
    circRNA = models.CharField("circRNA",max_length=500,null=True)
    method_of_circRNA_direction = models.CharField("method_of_circRNA_direction",max_length=500,null=True)
    expression_pattern = models.CharField("expression_pattern",max_length=100,null=True)
    Chromosome = models.CharField("Chromosome",max_length=100,null=True)
    Region = models.CharField("Region",max_length = 100,null = True )
    Strand = models.CharField("Strand",max_length = 100,null = True )
    Gene_Symbol = models.CharField("Gene_Sym",max_length= 100,null=True)
    host_gene = models.CharField("host_gene",max_length=100,null=True)
    tissue_or_cell_line = models.CharField("tissue_cell",max_length=100,null=True)
    Transcription_interval = models.CharField("Transcription_interval",max_length=200,null=True)
    Sequence = models.CharField("Sequence", max_length=500,null=True)