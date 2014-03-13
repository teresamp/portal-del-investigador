# -*- encoding: UTF-8 -*-

from django.core.management.base import BaseCommand, CommandError
from get_datos_departamento import Get_datos_departamento
from informe_pdf import Informe_pdf
from optparse import make_option
from viinvDB.models import GrupoinvestDepartamento


class Command(BaseCommand):
    help = u'Genera un PDF con los datos de un Departamento'
    option_list = BaseCommand.option_list + (
        make_option(
            "-y",
            "--year",
            dest="year",
            help="Specify the year in format YYYY",
        ),
        make_option(
            "-i",
            "--id",
            dest="id",
            help="Specify the ID of the Department",
        ),
    )

    def checkArgs(self, options):
        if not options['year']:
            raise CommandError("Option `--year=YYYY` must be specified.")
        else:
            self.year = options['year']

        if not options['id']:
            raise CommandError("Option `--id=X` must be specified.")
        else:
            self.deptID = options['id']

    def getData(self):
        data_dept = Get_datos_departamento(self.deptID, self.year)
        dept = GrupoinvestDepartamento.objects.get(id=self.deptID)
        invs = data_dept.get_investigadores()
        produccion = {}  # data_dept.get_produccion()
        actividad = {}  # data_dept.get_actividad()
        return dept, invs, produccion, actividad

    def create_report(self):
        dept, invs, produccion, actividad = self.getData()
        informe = Informe_pdf(self.year, dept, invs, produccion, actividad)
        informe.go()

    def handle(self, *args, **options):
        self.checkArgs(options)
        self.create_report()
