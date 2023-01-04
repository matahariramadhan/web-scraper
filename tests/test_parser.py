import pathlib
import pytest
from web_scraper import ShamelaParser


class TestShamelaParser:
    @pytest.fixture
    def markup(self) -> str:
        raw_html: str = ''

        with pathlib.Path('tests/samples/markup.html').open('r') as file:
            raw_html = file.read()
        return raw_html

    @pytest.fixture
    def shamela_parser(self, markup) -> ShamelaParser:
        shamela_parser = ShamelaParser()
        shamela_parser.parse_content(markup)
        return shamela_parser

    def test_can_parse_page_number(self, shamela_parser):
        actual = shamela_parser.page_number
        expected = '621'

        assert actual == expected

    def test_can_parse_fihris(self, shamela_parser):
        actual = shamela_parser.fihris
        expected = {
            'فهرس الكتاب': {
                'من سورة لقمان': '[سورة لقمان (٣١) : الآيات ١٤ إلى ١٥]'
            }
        }
        assert actual == expected

    def test_can_parse_hamesh(self, shamela_parser):
        actual = shamela_parser.hamesh
        expected = {
            1: '(١) في كتابه أحكام القرآن (٣/ ٣٥١) .',
            2: '(٢) الهداية شرح بداية المبتدي للإمام المرغيناني (١- ٢/ ٢٤٣) .'
        }

        assert actual == expected

    def test_can_parse_nass(self, shamela_parser):
        actual = shamela_parser.nass
        expected = {
            1: '<p><span class="anchor" id="p1"></span>وروي أنّ عثمان رضي الله عنه سأل الناس عن ذلك فقال له ابن عباس مثل ذلك، وأنّ عثمان رجع إلى قول علي وابن عباس، وحكى الجصاص <span style="color:#6c6c00">«١»</span> اتفاق أهل العلم على أنّ أقل مدة الحمل ستة أشهر.<a class="btn_tag btn btn-sm" href="#p1"><span class="text-gray fa fa-copy"></span></a></p>',
            2: '<p><span class="anchor" id="p2"></span>وذهب أبو حنيفة رحمه الله إلى أن مدة الرضاع المحرّم ثلاثون شهرا <span style="color:#6c6c00">«٢»</span> .<span style="color:#006d98"> لقوله تعالى:</span> وَحَمْلُهُ وَفِصالُهُ ثَلاثُونَ شَهْراً وسنبينه إن شاء الله. ثم إنه رحمه الله يحمل الآية التي معنا على الكثير الغالب في الفطام، إذ إنه لا يتجاوز به في العادة عامين، ويقول في آية البقرة إنها لبيان المدة التي تستحق فيها المطلقة أجرا على الإرضاع، إذ إنها لا تستحق أجرا فيما وراء العامين، وذلك لا ينفي أن يكون ما بعد العامين إلى تمام الثلاثين شهرا من مدة الرضاع المحرّم.<a class="btn_tag btn btn-sm" href="#p2"><span class="text-gray fa fa-copy"></span></a></p>',
            3: '<p><span class="anchor" id="p3"></span><span style="color:#006d98">وللحنفية في وجه الدلالة من قوله تعالى:</span> وَحَمْلُهُ وَفِصالُهُ ثَلاثُونَ شَهْراً على مذهب الإمام طريقتان:<a class="btn_tag btn btn-sm" href="#p3"><span class="text-gray fa fa-copy"></span></a></p>',
            4: '<p><span class="anchor" id="p4"></span><span style="color:#006d98">الأولى:</span> أنّه ذكر في الآية أمران متعاطفان أعقبا ببيان مدتهما،<span style="color:#006d98"> فتكون هذه المدة لكلّ من الأمرين استقلالا على ما يشهد به كلام الفقهاء في مثل قول المقرّ:</span> عليّ لكلّ من فلان وفلان مئة إلى سنة أنّ السنة أجل كلّ من الدينين، فتكون الثلاثون شهرا مدة كل من الحمل والرضاع، غير أنّه قد ثبت في الحمل ما أوجب نقصه من الثلاثين شهرا، وهو ما روي عن عائشة رضي الله عنها أنّ الولد لا يبقى في بطن أمه أكثر من سنتين، ولو بقدر فلكة مغزل، ومثل هذا لا يقال بالرأي، فله حكم الحديث المرفوع، وإذا كان الأمر كذلك بقيت مدة الفصال على ظاهرها.<a class="btn_tag btn btn-sm" href="#p4"><span class="text-gray fa fa-copy"></span></a></p>',
            5: '<p><span class="anchor" id="p5"></span><span style="color:#006d98">والطريقة الثانية:</span> في معنى قوله تعالى: وَحَمْلُهُ وَفِصالُهُ ثَلاثُونَ شَهْراً هي أن ليس المراد بالحمل هنا حمل الجنين في البطن، بل حمل الولد بعد الولادة في مدة الرضاع، وحينئذ تكون المدة المضروبة في الآية إنما هي لشيء واحد، هو ذلك الحمل الذي ينتهي بالفصال.<a class="btn_tag btn btn-sm" href="#p5"><span class="text-gray fa fa-copy"></span></a></p>',
            6: '<p><span class="anchor" id="p6"></span>وأنت تعلم أن العلماء ومنهم أبو حنيفة متفقون فيما حكى الجصاص على أنّ أقل مدة الحمل ستة أشهر،<span style="color:#006d98"> وأنهم استنبطوا ذلك من قوله تعالى:</span> وَحَمْلُهُ وَفِصالُهُ ثَلاثُونَ شَهْراً وقوله تعالى: وَفِصالُهُ فِي عامَيْنِ.<a class="btn_tag btn btn-sm" href="#p6"><span class="text-gray fa fa-copy"></span></a></p>',
            7: '<p><span class="anchor" id="p7"></span><span style="color:#006d98">فتأويل الحنفية آية الأحقاف وحملهم لها على الوجهين المتقدمين ينافي ما اتفق عليه الفقهاء جميعا ويلزمهم حينئذ أحد أمرين:</span> إما أن الإمام لم يوافق الجماعة في أنّ أقل<a class="btn_tag btn btn-sm" href="#p7"><span class="text-gray fa fa-copy"></span></a></p>'
        }

        assert actual == expected
