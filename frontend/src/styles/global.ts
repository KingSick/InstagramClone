import { createGlobalStyle } from 'styled-components';
import reset from 'styled-reset';

export default createGlobalStyle`
    ${reset}
    * {
        box-sizing: border-box;
    }
    html, body, #root {
        height: 100%;
        background-color: #FAFAFA;
    }
    a {
        all: unset;
    }
`;
