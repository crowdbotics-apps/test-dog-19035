import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import NotificationList83531Navigator from '../features/NotificationList83531/navigator';
import Settings83530Navigator from '../features/Settings83530/navigator';
import Settings83522Navigator from '../features/Settings83522/navigator';
import UserProfile83520Navigator from '../features/UserProfile83520/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
NotificationList83531: { screen: NotificationList83531Navigator },
Settings83530: { screen: Settings83530Navigator },
Settings83522: { screen: Settings83522Navigator },
UserProfile83520: { screen: UserProfile83520Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
