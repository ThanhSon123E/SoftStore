// Xử lý các tương tác trên giao diện SoftStore PC

document.addEventListener("DOMContentLoaded", function() {
    // Xác định ngôn ngữ hiện tại của trang web
    const currentLang = document.documentElement.getAttribute('lang') || 'vi';
    const langStrings = {
        vi: {
            connecting: 'Đang kết nối...',
            downloading: 'Đang tải...',
            started: 'Đã bắt đầu tải!'
        },
        en: {
            connecting: 'Connecting...',
            downloading: 'Downloading...',
            started: 'Download started!'
        }
    };
    const trans = langStrings[currentLang] || langStrings['vi'];
    
    // Đăng ký sự kiện tải xuống trên tất cả các nút download-btn
    const downloadBtns = document.querySelectorAll('.download-btn');
    
    downloadBtns.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            const downloadUrl = btn.getAttribute('href');
            const appId = btn.getAttribute('data-app-id');
            const btnTxtSpan = btn.querySelector('.btn-txt');
            const originalTxt = btnTxtSpan.innerText;
            
            if (btn.classList.contains('downloading')) {
                return;
            }
            
            // Đánh dấu trạng thái đang tải
            btn.classList.add('downloading');
            btnTxtSpan.innerText = trans.connecting;
            
            // Kích hoạt việc tải file thực tế từ Server ngay lập tức
            window.location.href = downloadUrl;

            // Cập nhật lượt tải bằng cách gọi API
            updateDownloadCount(appId, btn);
            
            // Tạo cấu trúc sóng nước
            const waveContainer = document.createElement('div');
            waveContainer.classList.add('wave-container');
            
            const waveOne = document.createElement('div');
            waveOne.classList.add('wave-item', 'wave-one');
            
            const waveTwo = document.createElement('div');
            waveTwo.classList.add('wave-item', 'wave-two');
            
            waveContainer.appendChild(waveOne);
            waveContainer.appendChild(waveTwo);
            btn.appendChild(waveContainer);
            
            // Chạy tiến trình tải dâng sóng từ từ làm hiệu ứng trực quan
            let progress = 0;
            const interval = setInterval(function() {
                progress += 4;
                
                // Ánh xạ tiến trình từ 0 -> 100% thành giá trị bottom từ -200% -> -40%
                let bottomVal = -200 + (160 * progress / 100);
                waveOne.style.bottom = bottomVal + '%';
                waveTwo.style.bottom = bottomVal + '%';
                
                btnTxtSpan.innerText = `${trans.downloading} ${progress}%`;
                
                if (progress >= 100) {
                    clearInterval(interval);
                    
                    // Thông báo tải thành công
                    btnTxtSpan.innerText = trans.started;
                    
                    // Tạo hiệu ứng mờ dần sóng nước
                    waveContainer.style.opacity = '0';
                    waveContainer.style.transition = 'opacity 0.4s ease';
                    
                    setTimeout(function() {
                        waveContainer.remove();
                        btn.classList.remove('downloading');
                        btnTxtSpan.innerText = originalTxt;
                    }, 2000);
                }
            }, 100); // 100ms * 25 bước = 2.5 giây dâng đầy sóng nước
        });
    });
    
    // Gọi API để cập nhật và tăng số lượt tải xuống
    function updateDownloadCount(appId, buttonElement) {
        if (!appId) return;
        
        fetch(`/api/download-count/${appId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Cập nhật hiển thị số lượt tải trên giao diện
                const card = buttonElement.closest('.app-card') || document.querySelector('.detail-main-card');
                if (card) {
                    const countEl = card.querySelector('.download-count-val');
                    if (countEl) {
                        countEl.innerText = data.new_count.toLocaleString();
                    }
                }
            }
        })
        .catch(err => console.error("Lỗi cập nhật lượt tải:", err));
    }

    // Xử lý khi thay đổi phiên bản trên các card phần mềm tại trang chủ
    const cardVersionSelects = document.querySelectorAll('.card-version-select');
    cardVersionSelects.forEach(select => {
        select.addEventListener('change', function() {
            const selectedVer = select.value;
            const slug = select.getAttribute('data-slug');
            const card = select.closest('.app-card');
            const downloadBtn = card.querySelector('.download-btn');
            
            // Cập nhật URL tải xuống tương ứng phiên bản đã chọn
            downloadBtn.setAttribute('href', `/download/${slug}?v=${encodeURIComponent(selectedVer)}`);
            
            // Cập nhật hiển thị dung lượng file tương ứng phiên bản đã chọn
            const selectedOption = select.options[select.selectedIndex];
            const size = selectedOption.getAttribute('data-size');
            if (size) {
                const sizeEl = card.querySelector('.card-file-size');
                if (sizeEl) {
                    sizeEl.innerText = size;
                }
            }
        });
    });

    // Xử lý khi thay đổi phiên bản trên trang chi tiết phần mềm
    const detailVersionSelect = document.getElementById('versionSelect');
    if (detailVersionSelect) {
        detailVersionSelect.addEventListener('change', function() {
            const selectedVer = detailVersionSelect.value;
            const slug = detailVersionSelect.getAttribute('data-slug');
            const downloadBtn = document.querySelector('.detail-sidebar-card .download-btn');
            
            // Cập nhật URL tải xuống tương ứng phiên bản đã chọn
            downloadBtn.setAttribute('href', `/download/${slug}?v=${encodeURIComponent(selectedVer)}`);
            
            // Cập nhật hiển thị dung lượng file trên sidebar chi tiết
            const selectedOption = detailVersionSelect.options[detailVersionSelect.selectedIndex];
            const size = selectedOption.getAttribute('data-size');
            if (size) {
                const sizeEl = document.querySelector('.detail-file-size');
                if (sizeEl) {
                    sizeEl.innerText = size;
                }
            }
        });
    }

    // Hiệu ứng thanh cuộn tiến trình trên đầu và thu gọn header khi cuộn chuột xuống
    window.addEventListener('scroll', function() {
        const header = document.querySelector('.app-header');
        const scrollProgress = document.getElementById('scrollProgress');
        
        if (header) {
            if (window.scrollY > 20) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
        
        if (scrollProgress) {
            const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
            scrollProgress.style.width = scrolled + '%';
        }
    });

    // Tối ưu hóa tìm kiếm tức thời (Live Instant Search)
    const searchForm = document.querySelector('.search-box');
    const searchInput = document.querySelector('.search-box input[name="q"]');
    const cards = document.querySelectorAll('.app-card');
    const noResults = document.getElementById('noResults');

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = searchInput.value.toLowerCase().trim();
            let visibleCount = 0;

            cards.forEach(card => {
                const name = card.querySelector('.app-name a').innerText.toLowerCase();
                const dev = card.querySelector('.app-developer').innerText.toLowerCase();
                const desc = card.querySelector('.app-description').innerText.toLowerCase();

                // Kiểm tra xem card có khớp với từ khóa tìm kiếm hay không
                const isMatch = name.includes(query) || dev.includes(query) || desc.includes(query);

                if (isMatch) {
                    card.style.display = 'flex';
                    card.classList.add('search-match');
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                    card.classList.remove('search-match');
                }
            });

            if (noResults) {
                if (visibleCount === 0) {
                    noResults.style.display = 'block';
                } else {
                    noResults.style.display = 'none';
                }
            }
        });
    }

    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
        });
    }

    // Logic thay đổi Theme Sáng/Tối với hiệu ứng Thanos Snap và View Transitions
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', (e) => {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            // Lấy tọa độ của nút bấm làm tâm xuất phát cho hiệu ứng quét
            const rect = themeToggle.getBoundingClientRect();
            const originX = rect.left + rect.width / 2;
            const originY = rect.top + rect.height / 2;
            
            // Truyền tọa độ này vào biến CSS
            document.documentElement.style.setProperty('--transition-origin-x', `${originX}px`);
            document.documentElement.style.setProperty('--transition-origin-y', `${originY}px`);

            // Tạo Canvas vẽ hạt bụi Thanos che phủ
            const canvas = document.createElement('canvas');
            canvas.style.position = 'fixed';
            canvas.style.top = '0';
            canvas.style.left = '0';
            canvas.style.width = '100vw';
            canvas.style.height = '100vh';
            canvas.style.pointerEvents = 'none';
            canvas.style.zIndex = '999999';
            document.body.appendChild(canvas);
            
            const ctx = canvas.getContext('2d');
            const scale = window.devicePixelRatio || 1;
            canvas.width = window.innerWidth * scale;
            canvas.height = window.innerHeight * scale;
            ctx.scale(scale, scale);
            
            const particles = [];
            const duration = 3000; // Hiệu ứng Thanos chậm rãi bi tráng dài 3 giây
            const maxRadius = Math.sqrt(Math.pow(window.innerWidth, 2) + Math.pow(window.innerHeight, 2)) * 1.1;
            
            // Hàm chuyển đổi màu CSS bất kỳ thành màu tro tàn cháy rụi (blend 75% xám tro sẫm, 25% sắc thái gốc)
            function blendToAsh(cssColor) {
                let r = 80, g = 80, b = 80; // Mặc định xám đậm
                
                if (cssColor.startsWith('rgb')) {
                    const matches = cssColor.match(/\d+/g);
                    if (matches && matches.length >= 3) {
                        r = parseInt(matches[0]);
                        g = parseInt(matches[1]);
                        b = parseInt(matches[2]);
                    }
                } else if (cssColor.startsWith('#')) {
                    let hex = cssColor.slice(1);
                    if (hex.length === 3) {
                        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
                    }
                    if (hex.length === 6) {
                        r = parseInt(hex.slice(0, 2), 16);
                        g = parseInt(hex.slice(2, 4), 16);
                        b = parseInt(hex.slice(4, 6), 16);
                    }
                }
                
                // Công thức tính độ sáng Grayscale chuẩn
                const gray = 0.299 * r + 0.587 * g + 0.114 * b;
                
                // Blend sang màu tro của phim Marvel (đất nung xám đen trầm)
                const ashR = Math.floor(gray * 0.75 + r * 0.25);
                const ashG = Math.floor((gray * 0.95) * 0.75 + g * 0.25);
                const ashB = Math.floor((gray * 0.9) * 0.75 + b * 0.25);
                
                return `rgb(${ashR}, ${ashG}, ${ashB})`;
            }

            // Định nghĩa hạt bụi/vảy tro tàn Thanos lững lờ cuốn theo gió
            class AshParticle {
                constructor(x, y) {
                    this.x = x;
                    this.y = y;
                    
                    // Vận tốc gốc: Bay nhẹ chéo sang phải và bốc lên trên
                    this.vx = 0.3 + Math.random() * 1.0;   // Sang phải
                    this.vy = -0.4 - Math.random() * 0.8;  // Lên trên
                    
                    // Thiết lập tần số nhiễu loạn gió hình sin để hạt bụi uốn lượn lơ lửng tự nhiên
                    this.windPhase = Math.random() * Math.PI * 2;
                    this.windSpeed = 0.02 + Math.random() * 0.04;
                    this.windAmp = 0.5 + Math.random() * 0.6;
                    this.time = 0;
                    
                    // Trích xuất màu sắc DOM gốc
                    let baseColor = 'rgb(90, 85, 80)';
                    let isText = false;
                    
                    const el = document.elementFromPoint(x, y);
                    if (el) {
                        const tagName = el.tagName.toLowerCase();
                        const style = window.getComputedStyle(el);
                        
                        const isHeading = ['h1', 'h2', 'h3', 'h4'].includes(tagName);
                        isText = ['p', 'span', 'a', 'li'].includes(tagName);
                        
                        let tempColor = isText || isHeading ? style.color : style.backgroundColor;
                        
                        // Leo lên cha nếu gặp nền trong suốt
                        let parent = el.parentElement;
                        while (parent && (tempColor === 'rgba(0, 0, 0, 0)' || tempColor === 'transparent' || tempColor === '')) {
                            const pStyle = window.getComputedStyle(parent);
                            tempColor = pStyle.backgroundColor;
                            parent = parent.parentElement;
                        }
                        if (tempColor && tempColor !== 'rgba(0, 0, 0, 0)' && tempColor !== 'transparent') {
                            baseColor = tempColor;
                        }
                    }
                    
                    // Chuyển màu gốc sang màu tro tàn cháy xám đen
                    this.color = blendToAsh(baseColor);
                    
                    // Đa dạng hóa cấu trúc hạt: vảy tro lớn méo mó và bụi mịn nhỏ
                    const rand = Math.random();
                    if (rand > 0.88) {
                        // Vảy tro lớn hình dạng bất định xoay tròn lơ lửng
                        this.size = 3.5 + Math.random() * 3.5;
                        this.isFlake = true;
                        this.rotation = Math.random() * Math.PI * 2;
                        this.rotSpeed = (Math.random() - 0.5) * 0.08;
                    } else if (rand > 0.5) {
                        // Hạt bụi tro vừa
                        this.size = 1.8 + Math.random() * 1.5;
                        this.isFlake = false;
                    } else {
                        // Bụi mịn nhỏ li ti
                        this.size = 0.8 + Math.random() * 1.0;
                        this.isFlake = false;
                    }
                    
                    if (isText) {
                        this.size *= 0.65; // Hạt cực nhỏ từ text
                    }
                    
                    this.alpha = 1.0;
                    this.life = 90 + Math.random() * 80; // Thời gian sống lâu để bay lượn xa
                    this.maxLife = this.life;
                }
                
                update() {
                    this.time++;
                    
                    // Lực gió nhiễu loạn hình sin/cos tạo hiệu ứng cuộn tro bay uốn lượn
                    const windX = Math.sin(this.windPhase + this.time * this.windSpeed) * this.windAmp;
                    const windY = Math.cos(this.windPhase + this.time * this.windSpeed * 0.7) * (this.windAmp * 0.4);
                    
                    this.x += this.vx + windX;
                    this.y += this.vy + windY;
                    
                    // Lực cản không khí nhẹ giữ tro bay lững lờ
                    this.vx *= 0.985;
                    this.vy *= 0.985;
                    
                    // Bay bổng bốc lên cao nhẹ
                    this.vy -= 0.005;
                    
                    // Xoay vảy tro
                    if (this.isFlake) {
                        this.rotation += this.rotSpeed;
                    }
                    
                    this.life--;
                    this.alpha = Math.max(0, this.life / this.maxLife);
                }
                
                draw(c) {
                    c.save();
                    c.globalAlpha = this.alpha;
                    c.fillStyle = this.color;
                    
                    // Bóng đổ nhẹ cho vảy tro để có chiều sâu
                    c.shadowColor = 'rgba(0, 0, 0, 0.25)';
                    c.shadowBlur = 2;
                    
                    if (this.isFlake) {
                        // Vẽ vảy tro đa giác ngẫu nhiên méo mó xoay tròn
                        c.translate(this.x, this.y);
                        c.rotate(this.rotation);
                        c.beginPath();
                        c.moveTo(-this.size, -this.size * 0.5);
                        c.lineTo(this.size * 0.8, -this.size);
                        c.lineTo(this.size * 1.2, this.size * 0.6);
                        c.lineTo(-this.size * 0.4, this.size * 1.1);
                        c.closePath();
                        c.fill();
                    } else {
                        // Vẽ hạt bụi tròn hoặc vuông nhỏ
                        c.beginPath();
                        if (Math.random() > 0.4) {
                            c.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                        } else {
                            c.rect(this.x - this.size, this.y - this.size, this.size * 2, this.size * 2);
                        }
                        c.fill();
                    }
                    
                    c.restore();
                }
            }
            
            let start = null;
            function runParticles(timestamp) {
                if (!start) start = timestamp;
                const progress = timestamp - start;
                const p = Math.min(progress / duration, 1);
                
                // easeOutQuad
                const easeVal = p * (2 - p);
                const currentRadius = easeVal * maxRadius;
                
                // Sinh hạt bụi dọc theo đường ranh giới quét theme
                if (p < 0.98) {
                    const circumference = 2 * Math.PI * currentRadius;
                    // Mật độ hạt thưa và lững lờ lướt gió
                    const numToSpawn = Math.min(Math.floor(circumference / 68) + 1, 14);
                    
                    for (let i = 0; i < numToSpawn; i++) {
                        const theta = Math.random() * Math.PI * 2;
                        const px = originX + currentRadius * Math.cos(theta);
                        const py = originY + currentRadius * Math.sin(theta);
                        
                        if (px >= 0 && px <= window.innerWidth && py >= 0 && py <= window.innerHeight) {
                            particles.push(new AshParticle(px, py));
                        }
                    }
                }
                
                ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
                
                for (let i = particles.length - 1; i >= 0; i--) {
                    const part = particles[i];
                    part.update();
                    part.draw(ctx);
                    if (part.life <= 0) {
                        particles.splice(i, 1);
                    }
                }
                
                if (p < 1 || particles.length > 0) {
                    requestAnimationFrame(runParticles);
                } else {
                    canvas.remove();
                }
            }

            // Thực hiện chuyển theme dùng View Transitions API kết hợp sinh bụi
            if (document.startViewTransition) {
                document.startViewTransition(() => {
                    document.documentElement.setAttribute('data-theme', newTheme);
                    localStorage.setItem('theme', newTheme);
                });
                requestAnimationFrame(runParticles);
            } else {
                // Fallback nếu trình duyệt không hỗ trợ View Transition
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
            }
        });
    }
});
