"""
    All from parameters part
"""
from kivy.properties import ObjectProperty, Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.selectioncontrol import MDCheckbox

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import IRightBodyTouch

from parametersPart.calculator import cuttingSpeed, spindleSpeed, metalRemovalRate, timeInCut


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass

########################################
# All main screen from parameters
########################################

class TurningScreen(Screen):
    """"""
    pass


class MillingScreen(Screen):
    """"""
    pass


class DrillingScreen(Screen):
    """"""
    pass


class TappingScreen(Screen):
    """"""
    pass


class ReamingScreen(Screen):
    """"""
    pass


class TolerancesScreen(Screen):
    """"""
    pass

##############################################
# All main screen from turning
# All calculate function-> calculator.py
##############################################


class MyScreen(Screen):
    """Class for all screen containing calculation of parameters."""
    score = ObjectProperty(None)
    machined_diameter = ObjectProperty(None)
    spindle_speed = ObjectProperty(None)
    depth_of_cut = ObjectProperty(None)
    feed_per_revolution = ObjectProperty(None)
    cutting_speed = ObjectProperty(None)
    length_of_cut = ObjectProperty(None)
    start_diameter = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # add Clock function to MyScreen class
        # submit - calculating function the cutting parameter
        Clock.schedule_interval(self.submit, .1)

    @staticmethod
    def input_text_service(*args):
        """Method that changes text type to float"""
        value = list(map(float, args))  # give a list of values

        return value


class CuttingSpeedScreen(MyScreen):
    """Class represents the screen for calculating the cutting speed in turning."""

    def submit(self, *args):
        """
        The method processes the given data and calls the functions for calculating the cutting speed.
        """
        if self.machined_diameter.text and self.spindle_speed.text:
            # use the static method and change value
            md, ss = MyScreen.input_text_service(self.machined_diameter.text, self.spindle_speed.text)
            # call functions to calculate cutting speed and get the result
            self.score.text = f'{cuttingSpeed(md, ss):.2f}'
        else:
            self.score.text = '0'


class SpindleSpeedScreen(MyScreen):
    """Class represents the screen for calculating the spindle speed in turning."""

    def submit(self, *args):
        """
        The method processes the given data and calls the functions for calculating the spindle speed.
        """
        if self.machined_diameter.text and self.cutting_speed.text:
            # use the static method and change value
            md, cs = MyScreen.input_text_service(self.machined_diameter.text, self.cutting_speed.text)
            # call functions to calculate spindle speed and get the result
            self.score.text = f'{spindleSpeed(md, cs):.2f}'
        else:
            self.score.text = '0'


class MetalRemovalRateScreen(MyScreen):
    """Class represents the screen for calculating the metal removal rate in turning."""

    def submit(self, *args):
        """
        The method processes the given data and calls the functions for calculating the metal removal rate.
        """
        if self.depth_of_cut.text and self.feed_per_revolution.text and self.cutting_speed.text:
            # use the static method and change value
            doc, fpr, cs = MyScreen.input_text_service(self.depth_of_cut.text,
                                                       self.feed_per_revolution.text,
                                                       self.cutting_speed.text, )
            # call functions to calculate metal removal rate and get the result
            self.score.text = f'{metalRemovalRate(doc, fpr, cs):.2f}'
        else:
            self.score.text = '0'


from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    check = ObjectProperty(None)

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class MyMDRaisedButton(MDRaisedButton):
    pass


class PowerRequirementScreen(MyScreen):
    """Class represents the screen for calculating the power requirement in turning."""
    field = ObjectProperty(None)
    check = ObjectProperty(None)

    # def on_checkbox_active(self):
    #
    #     self.show_MDDialog("5")
    #
    # def show_MDDialog(self, result):
    #     dialog = MDDialog(
    #         title="Phone ringtone",
    #         type="confirmation",
    #         size_hint=[.8, .8],
    #         items=[
    #             ItemConfirm(text="90"),
    #             ItemConfirm(text="80"),
    #             ItemConfirm(text="70"),
    #             ItemConfirm(text="60"),
    #             ItemConfirm(text="50"),
    #             ItemConfirm(text="40"),
    #             ItemConfirm(text="30"),
    #             ItemConfirm(text="20"),
    #             ItemConfirm(text="10"),
    #             ItemConfirm(text="5"),
    #             ItemConfirm(text="0"),
    #         ],
    #         buttons=[
    #             MyMDRaisedButton(),
    #         ],
    #     )
    #     dialog.open()

    def submit(self, *args):
        pass

    # def set_value(self, instance):
    #     def set_value(interval):
    #         if instance:
    #
    #             self.field.text = instance
    #         else:
    #             self.field.text = '0'
    #
    #     Clock.schedule_once(set_value, 0.5)


class TimeInScreen(MyScreen):
    """Class represents the screen for calculating the time in cut in turning."""

    def submit(self, *args):
        """
        The method processes the given data and calls the functions for calculating the time in cut.
        """
        if (self.start_diameter.text and self.cutting_speed.text and self.depth_of_cut.text
                and self.length_of_cut.text and self.machined_diameter and self.feed_per_revolution):
            # use the static method and change value
            sd, cs, soc, loc, md, fpr, = MyScreen.input_text_service(self.start_diameter.text,
                                                                     self.cutting_speed.text,
                                                                     self.depth_of_cut.text,
                                                                     self.length_of_cut.text,
                                                                     self.machined_diameter,
                                                                     self.feed_per_revolution, )
            # call functions to calculate time in cut and get the result
            self.score.text = f'{timeInCut(sd, cs, soc, loc, md, fpr):.2f}'
        else:
            self.score.text = '0'


#################################
# All main screen from milling, Add!!!
#################################

class MillingCuttingSpeedScreen(MyScreen):
    pass


class MillingSpindleSpeedScreen(MyScreen):
    pass


class MillingTableFeedScreen(MyScreen):
    pass


class MillingRemovalRateScreen(MyScreen):
    pass


class MillingTimeInCutScreen(MyScreen):
    pass


class MillingTotalCycleTimeScreen(MyScreen):
    pass


class MillingPowerRequirement(MyScreen):
    pass


#################################
# All main screen from drilling, Add!!
################################

class DrillingCuttingSpeedScreen(MyScreen):
    pass


class DrillingFeedForceScreen(MyScreen):
    pass


class DrillingFeedSpeedScreen(MyScreen):
    pass


class DrillingPowerRequirementScreen(MyScreen):
    pass


class DrillingTimeINCutScreen(MyScreen):
    pass


class DrillingTotalCycleTimeScreen(MyScreen):
    pass


#################################
# All main screen from tapping, Add!!
################################

class TappingCuttingScreen(MyScreen):
    pass


class TappingPenetrationRateScreen(MyScreen):
    pass


class TappingSpindleSpeedScreen(MyScreen):
    pass


class TappingTimeInCutScreen(MyScreen):
    pass


class TappingTotalCycleTime(MyScreen):
    pass


################################################
# All main screen from reaming, Add!!
################################################

# Add !!!

