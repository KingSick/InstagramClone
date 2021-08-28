import React, { ReactElement } from 'react';
import { Switch, Route } from 'react-router-dom';

import MainPage from './main';

export default (): ReactElement => (
  <Switch>
    <Route exact path="/" component={MainPage} />
  </Switch>
);
