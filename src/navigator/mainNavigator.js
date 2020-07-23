import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import ArticleList83588Navigator from '../features/ArticleList83588/navigator';
import ArticleList83587Navigator from '../features/ArticleList83587/navigator';
import ArticleList83586Navigator from '../features/ArticleList83586/navigator';
import UserProfile83560Navigator from '../features/UserProfile83560/navigator';
import Tutorial83559Navigator from '../features/Tutorial83559/navigator';
import NotificationList83531Navigator from '../features/NotificationList83531/navigator';
import Settings83530Navigator from '../features/Settings83530/navigator';
import Settings83522Navigator from '../features/Settings83522/navigator';
import UserProfile83520Navigator from '../features/UserProfile83520/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
ArticleList83588: { screen: ArticleList83588Navigator },
ArticleList83587: { screen: ArticleList83587Navigator },
ArticleList83586: { screen: ArticleList83586Navigator },
UserProfile83560: { screen: UserProfile83560Navigator },
Tutorial83559: { screen: Tutorial83559Navigator },
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
