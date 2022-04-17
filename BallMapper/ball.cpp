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
const string FILENAME = "bm";
vector<string> tickerlist;

struct pt {
    int n;
    vector<long double> c;
    pt() {}
    pt(int n_, vector<long double> c_) {
        n = n_;
        swap(c,c_);
    }
};

struct ball {
    vector<int> sz;
    vector<pair<int, int> > ed;
    vector<vector<int> > poi; // [m] -> [n]
    vector<int> land;
    vector<long double> cl;
    vector<vector<int> > cov; // [n] -> [m]
    vector<int> wei;
    ball(){}
};

long double dist(struct pt a, struct pt b) {
    // assert(a.n==b.n);
    if(a.n != b.n) return -1;
    assert(a.n == a.c.size() && b.n == b.c.size());
    long double dis = 0;
    for(int i = 0;i < a.n;i++) {
        dis += (a.c[i] - b.c[i]) * (a.c[i] - b.c[i]);
    }
    // dis = dis/(long double)a.n;
    dis = sqrt(dis);
    return dis;
}

ball ballmap(vector<struct pt> pts, vector<long double> val, long double eps) {
    int n = pts.size();
    int m = 0; // no. of landmarks. THIS IS 0-INDEXED!
    vector<vector<int> > cov, poi;
    cov.assign(n,{});
    vector<long double> cl;
    vector<int> sz;
    struct ball bal;
    vector<int> land;
    vector<int> wei;
    vector<pair<int, int> > ed, ed0;
    int ind = 0;


    while(ind < n) {
        land.push_back(ind);
        for(int j = 0;j < n;j++) {
            long double dis = dist(pts[ind], pts[j]);
            assert(dis >= 0);
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
    // cerr << m << ln;
    poi.assign(m,{});
    cl.assign(m,{});

    for(int i = 0;i < n; i++) {
        for(int j = 0;j < cov[i].size(); j++) {
            poi[cov[i][j]].push_back(i);
        }
    }
    sz.assign(m,0);
    for(int i = 0;i < m;i++) {
        sz[i] = poi[i].size() + 2; // +2 for the two end points
    }
    for(int i = 0;i < m;i++) {
        long double avg = 0;
        for (int j = 0;j < poi[i].size();j++) {
            avg += val[poi[i][j]];
        }
        avg = avg/(long double)poi[i].size();
        cl[i] = avg;
    }
    
    for(int i = 0;i < n;i++) {
        for(int j = 0;j < cov[i].size();j++) {
            for(int k = j+1; k < cov[i].size();k++) {
                int fr, t0;
                fr = cov[i][j];
                t0 = cov[i][k];
                ed0.push_back({fr, t0});
            }
        }
    }
    sort(ed0.begin(), ed0.end());
    // fo(i, ed0.size()) {
    //     cerr << ed0[i].first << " " << ed0[i].second << endl;
    // }
    for(int i = 0;i < ed0.size();i++){
        int j = i;
        while(j < ed0.size() && ed0[i].first == ed0[j].first && ed0[i].second == ed0[j].second) j++;
        ed.push_back(ed0[i]);
        wei.push_back(j-i);
        i=j;
    }
    bal.cl = cl;
    bal.cov = cov;
    bal.poi = poi;
    bal.ed = ed;
    bal.land = land;
    bal.sz = sz;
    bal.wei = wei;
    
    return bal;
}

void balltofile (const struct ball &bal) {
    string pois = "../"+FILENAME+"_points_covered_by_landmarks";
    freopen( pois.c_str(), "w", stdout);
    for(int i = 0;i < bal.poi.size();i++) {
        for(int j = 0;j < bal.poi[i].size();j++) {
            cout << " " << bal.poi[i][j]+1;
        }
        cout << endl;
    }
    {
        string pois = "../"+FILENAME+"_points_covered_by_landmarks_tickers";
        freopen( pois.c_str(), "w", stdout);
        for(int i = 0;i < bal.poi.size();i++) {
            for(int j = 0;j < bal.poi[i].size();j++) {
                cout << " " << tickerlist[bal.poi[i][j]];
            }
            cout << endl;
        }
    }
    string ed = "../"+FILENAME+"_edges";
    freopen( ed.c_str(), "w", stdout);
    for (auto u: bal.ed) {
        cout << u.first+1 << " " << u.second+1 << endl;
    }
    string vert = "../"+FILENAME+"_vertices";
    freopen( vert.c_str(), "w", stdout);
    for(int  i =0;i < bal.sz.size(); i++) {
        cout << i+1<< " " <<bal.sz[i] << endl; 
    }
    string cl = "../"+FILENAME+"_coloring";
    freopen( cl.c_str(), "w", stdout);
    for(int i =0 ;i < bal.cl.size();i++) {
        cout << bal.cl[i] << endl;
    }
    string land = "../"+FILENAME + "_landmarks";
    freopen( land.c_str(), "w", stdout);
    for(int i = 0;i < bal.land.size();i++) {
        cout << bal.land[i]+1 << endl;
    }
    string land_tickers = "../"+FILENAME + "_landmarks_tickers";
    freopen( land_tickers.c_str(), "w", stdout);
    for(int i = 0;i < bal.land.size();i++) {
        cout << tickerlist[bal.land[i]] << endl;
    }
    string wei = "../"+FILENAME+"_edges_strength";
    freopen( wei.c_str(), "w", stdout);
    for(int i = 0;i < bal.wei.size();i++) {
        cout << bal.wei[i] << endl;
    }
}
vector<long double> csvlinetolist(string csvline) {
    // decode one line of csv
    vector<long double> res;
    stringstream ss(csvline);
    string item;
    // remove first item
    getline(ss, item, ','); //TODO: add back
    tickerlist.push_back(item);
    while(getline(ss, item, ',')) {
        res.push_back(stod(item));
    }
    return res;
}

int main(int argc, char** argv){   

    Nos;
    tickerlist.clear();
    long double eps = 0.2;
    if(argc == 3) {
        string year, qtr;
        year = argv[1];
        qtr = argv[2];
        string inputfilename =  "../data/QuarterlyRatiosCleanNormalised/" + year + "_Q" + qtr + ".csv";
        cerr << inputfilename << endl;
        freopen(inputfilename.c_str(), "r", stdin);
    } else if(argc == 4) {
        string year, qtr;
        year = argv[1];
        qtr = argv[2];
        eps = stod(argv[3]);
        string inputfilename =  "../data/QuarterlyRatiosCleanNormalised/" + year + "_Q" + qtr + ".csv";
        cerr << inputfilename << endl;
        freopen(inputfilename.c_str(), "r", stdin);
    } else {
        cerr << "BAD INPUT: " << argc << " going with 2017 Q1\n";
        // freopen("../data/QuarterlyRatiosCleanNormalised/2017_Q1.csv", "r", stdin);
        freopen("../BallMapper/data/boston.csv", "r", stdin);
        // freopen("../BallMapper/data/rand.csv", "r", stdin);
    }
    // cout << fixed << setprecision(25);

    auto st = clock();

    vector<struct pt> pts;
    vector<long double> val;
    // read csv
    string line;
    getline(cin, line);
    while(getline(cin, line)) {
        vector<long double> tmp = csvlinetolist(line);
        struct pt p;
        p.n = 0;
        for(auto u: tmp) {
            p.c.push_back(u);
            p.n++;
        }
        // remove last one, put in val
        p.n--;
        p.c.pop_back();
        pts.push_back(p);
        val.push_back(tmp.back());
    }
    // while(getline(cin, line)) {
    //     vector<long double> tmp = csvlinetolist(line);
    //     struct pt p;
    //     p.n = 0;
    //     for(auto u: tmp) {
    //         // cerr << u << " ";
    //         p.c.push_back(u);
    //         p.n++;
    //     }
    //     // cerr << ln;
    //     // remove last one, put in val
    //     p.n--;
    //     swap(p.c[1], p.c[2]);
    //     val.push_back(p.c[2]);
    //     p.c.pop_back();
    //     pts.push_back(p);
    // }
    cerr << val.size() << " " << pts.size() << ln;
    if (!pts.empty()) cerr << pts[0].c.size() << ln;
    ball b = ballmap(pts, val, eps);

    balltofile(b);

    auto en = clock();
    cerr << "time taken = " << (long double)(en - st)/CLOCKS_PER_SEC << "s" << ln;
    

    return 0;
}