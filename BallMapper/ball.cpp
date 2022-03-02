#include<bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
using namespace std;
typedef long long int ll;
typedef long double ld;
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define oset tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define Nos                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define fo(i,n) for(ll i=0;i<n;i++)
#define rfo(i,n) for(ll i = n;i >= 0;i--)
#define rfosn(i, s, n) for(ll i = n; i >= s; i--)
#define PI 3.141592654
#define all(v) (v).begin(), (v).end()
#define allr(v) (v).rbegin(), (v).rend()
#define pb push_back
#define mp make_pair
#define fosn(i, s, n) for(int i = s;i < n;i ++)
 
#define vb vector<bool>
#define vvb vector<vb>
#define vi vector<int>
#define vvi vector<vi>
#define vl vector<ll>
#define vvl vector<vl>
#define ln '\n'
#define pii pair<int,int>
#define vpi vector<pii>
// #define unordered_set(T) unordered_set<T, custom_hash>
// #define unordered_map(T1, T2) unordered_map<T1, T2, custom_hash>
#define f first
#define se second
#define out2(a1,a2) cout << a1 << " " << a2 << endl  

const ll md = 998244353 ;
//ll hash_prime = 31;
// const ll md = 998244353; // 1e9+7;
long long exp(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = (res * a) % m;
        a = (a * a) % m;
        b >>= 1;
    }
    return res%m;
}

ll C(ll n, ll k) {
    if(n < k) return 0;
    ll res = 1;
    for (int i = n - k + 1; i <= n; ++i)
        {res *= i; res %= md;}
    for (int i = 2; i <= k; ++i)
        {res *= exp(i, md-2, md); res %= md;}
    return res;
}

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
const int N = 3e5+3;

struct pt {
    int n;
    vector<double> c;
    pt() {}
    pt(int n_, vector<double> c_) {
        n = n_;
        swap(c,c_);
    }
};

struct ball {
    vector<int> sz;
    vector<pair<int, int> > ed;
    vector<vector<int> > poi; // [m] -> [n]
    vector<int> land;
    vector<double> cl;
    vector<vector<int> > cov; // [n] -> [m]
    ball(){}
};

double dist(struct pt a, struct pt b) {
    if(a.n != b.n) return -1;
    double dis = 0;
    for(int i = 0;i < a.n;i++) {
        dis += (a.c[i] - b.c[i]) * (a.c[i] - b.c[i]);
    }
    dis = dis/(double)a.n;
    dis = sqrt(dis);
    return dis;
}

ball ballmap(vector<struct pt> pts, vector<double> val, double eps) {
    int n = pts.size();
    int m = 0; // no. of landmarks. IT IS 0-INDEXED
    vector<vector<int> > cov, poi;
    vector<double> cl;
    vector<int> sz;
    cov.assign(n,{});
    struct ball bal;
    vector<int> land;
    vector<int> wei;
    vector<pair<int, int> > ed, ed0;
    int ind = 0;


    while(ind < n) {
        land.push_back(ind);
        for(int j = 0;j < n;j++) {
            double dis = dist(pts[ind], pts[j]);
            if(dis <= eps) {
                cov[j].push_back(m);
            }
        }
        while(true) {
            if(ind >= n) break;
            if(cov[ind].size() == 0) break;
            ind++;
        }
        m++;
    }
    poi.assign(m,{});
    cl.assign(m,{});

    for(int i = 0;i < n; i++) {
        for(int j = 0;j < cov[i].size(); j++) {
            poi[cov[i][j]].push_back(i);
        }
    }
    sz.assign(n,0);
    for(int i = 0;i < n;i++) {
        sz[i] = poi[i].size() + 2; // why +2 ??
    }
    for(int i = 0;i < m;i++) {
        double avg = 0;
        for (int j = 0;j < poi[i].size();j++) {
            avg += val[poi[i][j]];
        }
        avg = avg/(double)poi[i].size();
        cl[i] = avg;
    }
    
    // map<pair<int, int>, int> wei_map;
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < cov[i].size();j++) {
            for(int k = j+1; k < cov[i].size();k++) {
                int fr, t0;
                fr = cov[i][j];
                t0 = cov[i][k];
                ed0.push_back({fr, t0});
                // wei_map[{fr, t0}]++;
            }
        }
    }
    // for(const auto &u: wei_map) {
    //     ed.push_back({u.first.first, u.first.second});
    //     wei.push_back(u.second);
    // }
    sort(ed.begin(), ed0.end());
    for(int i = 0;i < ed0.size();i++){
        int j = i;
        while(j < ed0.size() && ed0[i] == ed0[j]) j++;
        ed.push_back(ed0[i]);
        wei.push_back(j-i);
    }
    bal.cl = cl;
    bal.cov = cov;
    bal.poi = poi;
    bal.ed = ed;
    bal.land = land;
    bal.sz = sz;
    
    return bal;
}

int main(){   

    Nos;
    freopen("data/boston.txt", "r", stdin);
    // cout << fixed << setprecision(25);

    auto st = clock();

    vector<struct pt> pts;
    vector<double> val;
    int n = 506;
    int m = 14;
    val.assign(n,0);
    fo(i,n) {
        struct pt po;
        po.n = m-1;
        po.c.assign(m-1, 0);
        fo(j,m-1) {
            cin >> po.c[j];
        }
        cin >> val[i];
    }
    double eps = 100;
    // ball b = ballmap(pts, val, eps);

    auto en = clock();
    cout << (double)(en - st) << ln;
    

    return 0;
}