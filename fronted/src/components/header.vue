<template>
    <header class="header-wrapper">
        <div class="container">
            <ul class="left-nav">
                <li>Cloud Document</li>
                <li
                        :class="{ 'active': navList[0].name === currentNav }"
                        @click="navItemClickHandler(navList[0])"
                >
                    {{ navList[0].name }}
                </li>
                <li
                        v-if="isLogin"
                        :class="{ 'active': navList[1].name === currentNav }"
                        @click="navItemClickHandler(navList[1])"
                >
                    {{ navList[1].name }}
                </li>
                <li 
                    @click="navItemClickHandler(navList[2])"
                    v-if="isLogin"
                >
                    Vip
                </li>

            </ul>
            <div class="login-info" v-if="isLogin">
                <span>
                    Welcome
                    <strong class="vip"> {{isVip?'vip':''}} </strong>
                    {{ account }}!
                </span>
                <span>|</span>
                <span @click="logout">Log out</span>
            </div>
        </div>
    </header>
</template>

<script>
    import {mapState} from 'vuex'

    export default {
        name: 'Header',
        data() {
            return {
                currentNav: 'upload files',
                navList: [
                    {
                        id: 0,
                        name: 'upload files',
                        link: '/'
                    },
                    {
                        id: 1,
                        name: 'download files',
                        link: '/download'
                    },
                    {
                        id: 2,
                        name: 'vip',
                        link: '/vip'
                    }
                ]
            }
        },
        methods: {
            logout() {
                this.$confirm('Are you sure you want to log out?', 'Tips', {
                    confirmButtonText: 'sure',
                    cancelButtonText: 'cancel',
                    type: 'warning'
                }).then(() => {
                    this.$store.dispatch('logout')
                    this.$router.push({path: "/"})
                })
            },
            navItemClickHandler(currentNav) {
                this.currentNav = currentNav.name
                this.$router.push({path: currentNav.link})
            }
        },
        computed: {
            ...mapState(['isLogin', 'account', 'isVip'])
        }
    }
</script>

<style lang="less">
    .header-wrapper {
        font-size: 14px;
        color: #9d9d9d;
        background-color: #222;
        background-image: linear-gradient(to bottom, #3c3c3c 0, #222 100%);
        height: 50px;
        line-height: 50px;

        &::after {
            display: block;
            clear: both;
            content: ' ';
        }

        .left-nav {
            float: left;

            &::after {
                display: block;
                clear: both;
                content: ' ';
            }

            :first-child {
                color: #ffffff;
                font-size: 18px;
                cursor: text;
            }

            li {
                cursor: pointer;
                float: left;
                padding: 0 8px;

                &.active {
                    background-color: #0E0E0E;
                    color: #ffffff;
                }

                &:hover {
                    color: #ffffff;
                }
            }
        }

        .login-info {
            float: right;

            span {
                margin-left: 15px;
                cursor: pointer;

                &:hover {
                    color: #ffffff;
                }
            }
        }
    }
    .vip {
        color: #23A7F2;
    }
</style>
