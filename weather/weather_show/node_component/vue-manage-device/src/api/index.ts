import request from '../utils/request';

export const fetchData = () => {
    return request({
        url: './table.json',
        method: 'get'
    });
};

export const requestData = (req_url:string, req_method:string) => {
    return request({
        url: req_url,
        method: req_method,
    });
};
