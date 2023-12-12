import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';
import { usePermissStore } from '../store/permiss';
import Home from '../views/home.vue';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/mainframe',
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        children: [
            {
                path: '/mainframe',
                name: 'mainframe',
                meta: {
                    title: '系统首页',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "mainframe" */ '../views/mainframe.vue'),
            },
            {
                path: '/deviceset',
                name: 'deviceset',
                meta: {
                    title: '设备设置',
                    permiss: '3',
                },
                component: () => import(/* webpackChunkName: "deviceset" */ '../views/deviceset.vue'),
            },
            {
                path: '/deviceshow',
                name: 'deviceshow',
                meta: {
                    title: '设备状态',
                    permiss: '2',
                },
                component: () => import(/* webpackChunkName: "deviceshow" */ '../views/deviceshow.vue'),
            },
            {
                path: '/tabs',
                name: 'tabs',
                meta: {
                    title: '系统消息',
                    permiss: '1',
                },
                component: () => import(/* webpackChunkName: "tabs" */ '../views/tabs.vue'),
            },
            {
                path: '/permission',
                name: 'permission',
                meta: {
                    title: '权限管理',
                    permiss: '4',
                },
                component: () => import(/* webpackChunkName: "permission" */ '../views/permission.vue'),
            },
            {
                path: '/user',
                name: 'user',
                meta: {
                    title: '个人中心',
                },
                component: () => import(/* webpackChunkName: "user" */ '../views/user.vue'),
            },  
        ],
    },
    {
        path: '/login',
        name: 'Login',
        meta: {
            title: '登录',
        },
        component: () => import(/* webpackChunkName: "login" */ '../views/login.vue'),
    },
    {
        path: '/403',
        name: '403',
        meta: {
            title: '没有权限',
        },
        component: () => import(/* webpackChunkName: "403" */ '../views/403.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | vue-manage-system`;
    const role = localStorage.getItem('ms_username');
    const permiss = usePermissStore();
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permiss && !permiss.key.includes(to.meta.permiss)) {
        // 如果没有权限，则进入403
        next('/403');
    } else {
        next();
    }
});

export default router;
