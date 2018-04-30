# Copyright 2018 Yacine BOUSLAHI
#
# This file is a skill for the MyCroft.AI. More information in the README file
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname
import requests
from bs4 import BeautifulSoup

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_wav

        
__author__ = 'yacinebs'
__name__ = 'SodexoPlaceSkill'

logger = getLogger(__name__)

class SodexoPlaceSkill(MycroftSkill):

    def __init__(self):
        super(SodexoPlaceSkill, self).__init__(name="SodexoPlaceSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        sodexo_place_intent = IntentBuilder("SodexoPlaceIntent").require("SodexoPlaceKeyword").build()
        self.register_intent(sodexo_place_intent, self.handle_sodexo_place_intent)

    def handle_sodexo_place_intent(self, message):
        play_wav(self.shutter_sound)
        #req = requests.get('http://sodexo-restauration.moneweb.fr')
        #soup = BeautifulSoup(req.text, "html.parser")
        #places_dispo = soup.find("div", {"class": "litPlacesDispo"})
        #places = places_dispo.get_text()
        places = "Currently 320 places available"
        self.speak(places)

    def stop(self):
        pass


def create_skill():
    return SodexoPlaceSkill()

#TODO : add french vocab file