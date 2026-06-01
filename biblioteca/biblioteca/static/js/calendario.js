jQuery.datetimepicker.setLocale('es');

jQuery('#id_fecha_publicacion').datetimepicker({
  i18n: {
    es: {
      months: [
        'Enero','Febrero','Marzo','Abril',
        'Mayo','Junio','Julio','Agosto',
        'Septiembre','Octubre','Noviembre','Diciembre'
      ],
      dayOfWeek: [
        "Domingo", "Lunes", "Martes", "Miércoles",
        "Jueves", "Viernes", "Sábado"
      ]
    }
  },
  timepicker: false,
  format: 'Y-m-d',
  lang: 'es'  // ✅ idioma en español
});