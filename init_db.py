from app import create_app
from models import db, Software, SoftwareVersion

app = create_app()

def seed_database():
    with app.app_context():
        # Làm sạch cơ sở dữ liệu và tạo bảng mới
        db.drop_all()
        db.create_all()
        
        print("Đang nạp danh sách phần mềm PC vào cơ sở dữ liệu...")
        
        software_list = [
            # Trình duyệt (browsers)
            {
                'name': 'Google Chrome',
                'slug': 'chrome',
                'version': '121.0.6167.140',
                'description': 'Trình duyệt web nhanh chóng, an toàn và dễ sử dụng nhất thế giới phát triển bởi Google.',
                'detail_description': 'Google Chrome là trình duyệt web miễn phí được hàng tỷ người sử dụng nhờ tốc độ tải trang cực nhanh, công cụ bảo mật tiên tiến tích hợp và kho tiện ích mở rộng (Extensions) khổng lồ hỗ trợ mọi nhu cầu làm việc, học tập.',
                'category': 'browsers',
                'developer': 'Google LLC',
                'file_size': '92.4 MB',
                'download_count': 125430,
                'icon_type': 'chrome',
                'download_filename': 'ChromeStandaloneSetup64.exe',
                'download_url': 'https://dl.google.com/chrome/install/ChromeStandaloneSetup64.exe',
                'versions': []
            },
            {
                'name': 'Mozilla Firefox',
                'slug': 'firefox',
                'version': '122.0.1',
                'description': 'Trình duyệt web mã nguồn mở, bảo vệ quyền riêng tư người dùng tối đa.',
                'detail_description': 'Mozilla Firefox là trình duyệt mã nguồn mở nổi tiếng với cam kết bảo mật quyền riêng tư tối đa cho người dùng. Khả năng chống theo dõi thông minh, tiêu tốn ít RAM và khả năng tùy biến giao diện linh hoạt.',
                'category': 'browsers',
                'developer': 'Mozilla Foundation',
                'file_size': '58.2 MB',
                'download_count': 45210,
                'icon_type': 'firefox',
                'download_filename': 'firefox_installer_x64.exe',
                'download_url': 'https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=vi',
                'versions': []
            },
            {
                'name': 'Brave Browser',
                'slug': 'brave',
                'version': '1.62.162',
                'description': 'Trình duyệt web tập trung bảo mật, chặn quảng cáo tự động và tăng tốc độ duyệt web.',
                'detail_description': 'Brave Browser tự động chặn quảng cáo và các trình theo dõi trực tuyến giúp tải trang nhanh hơn gấp 3 lần, tiết kiệm pin và băng thông. Đồng thời tích hợp tính năng bảo mật nâng cao và ví điện tử Web3 an toàn.',
                'category': 'browsers',
                'developer': 'Brave Software',
                'file_size': '110 MB',
                'download_count': 31400,
                'icon_type': 'brave',
                'download_filename': 'BraveBrowserSetup.exe',
                'download_url': 'https://laptop-updates.brave.com/latest/winx64',
                'versions': []
            },
            
            # Lập trình (dev)
            {
                'name': 'Visual Studio Code',
                'slug': 'vscode',
                'version': '1.86.1',
                'description': 'Trình soạn thảo mã nguồn gọn nhẹ nhưng mạnh mẽ nhất cho lập trình viên.',
                'detail_description': 'Visual Studio Code (VS Code) là IDE soạn thảo mã nguồn miễn phí chạy trên Windows, macOS và Linux. Tích hợp sẵn Git, hỗ trợ debug trực quan, kho plug-in phong phú hỗ trợ viết code HTML, JS, Python, C++, v.v.',
                'category': 'dev',
                'developer': 'Microsoft Corporation',
                'file_size': '90.1 MB',
                'download_count': 98650,
                'icon_type': 'vscode',
                'download_filename': 'VSCodeUserSetup-x64.exe',
                'download_url': 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user',
                'versions': [
                    {'version': '1.86.1', 'download_url': 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user', 'file_size': '90.1 MB'},
                    {'version': '1.85.2', 'download_url': 'https://update.code.visualstudio.com/1.85.2/win32-x64-user/stable', 'file_size': '88.5 MB'}
                ]
            },
            {
                'name': 'Python SDK',
                'slug': 'python',
                'version': '3.12.2',
                'description': 'Bộ cài đặt ngôn ngữ lập trình Python và trình thông dịch chính thức.',
                'detail_description': 'Python là ngôn ngữ lập trình đa năng, dễ học và vô cùng mạnh mẽ được dùng phổ biến trong AI, phân tích dữ liệu và phát triển web. Bộ cài đặt chứa sẵn trình thông dịch Python, thư viện chuẩn và công cụ quản lý thư viện pip.',
                'category': 'dev',
                'developer': 'Python Software Foundation',
                'file_size': '25.4 MB',
                'download_count': 64100,
                'icon_type': 'python',
                'download_filename': 'python-3.12.2-amd64.exe',
                'download_url': 'https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe',
                'versions': [
                    {'version': '3.12.2', 'download_url': 'https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe', 'file_size': '25.4 MB'},
                    {'version': '3.11.8', 'download_url': 'https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe', 'file_size': '24.2 MB'},
                    {'version': '3.10.11', 'download_url': 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe', 'file_size': '27.6 MB'}
                ]
            },
            {
                'name': 'Git Version Control',
                'slug': 'git',
                'version': '2.43.0',
                'description': 'Hệ thống quản lý phiên bản phân tán miễn phí dành cho các dự án phần phần mềm.',
                'detail_description': 'Git là tiêu chuẩn công nghiệp về quản lý mã nguồn và theo dõi lịch sử thay đổi của dự án. Hỗ trợ làm việc nhóm hiệu quả, phân nhánh (branching) thông minh và tương thích tuyệt đối với GitHub, GitLab.',
                'category': 'dev',
                'developer': 'Git Community',
                'file_size': '57.8 MB',
                'download_count': 38200,
                'icon_type': 'git',
                'download_filename': 'Git-2.43.0-64-bit.exe',
                'download_url': 'https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe',
                'versions': [
                    {'version': '2.43.0', 'download_url': 'https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe', 'file_size': '57.8 MB'},
                    {'version': '2.42.0', 'download_url': 'https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.1/Git-2.42.0-64-bit.exe', 'file_size': '56.4 MB'}
                ]
            },
            {
                'name': 'XAMPP Developer',
                'slug': 'xampp',
                'version': '8.2.12',
                'description': 'Môi trường phát triển PHP tích hợp sẵn Apache, MariaDB, PHP và Perl cực kỳ phổ biến.',
                'detail_description': 'XAMPP là bộ công cụ hoàn hảo giúp các nhà phát triển web xây dựng máy chủ web cục bộ một cách dễ dàng và nhanh chóng chỉ bằng một cú nhấp chuột. Thích hợp cho việc lập trình và thử nghiệm mã nguồn PHP.',
                'category': 'dev',
                'developer': 'Apache Friends',
                'file_size': '149 MB',
                'download_count': 42800,
                'icon_type': 'xampp',
                'download_filename': 'xampp-windows-x64-8.2.12-0-installer.exe',
                'download_url': 'https://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/8.2.12/xampp-windows-x64-8.2.12-0-VS16-installer.exe',
                'versions': [
                    {'version': '8.2.12 (PHP 8.2)', 'download_url': 'https://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/8.2.12/xampp-windows-x64-8.2.12-0-VS16-installer.exe', 'file_size': '149 MB'},
                    {'version': '8.1.25 (PHP 8.1)', 'download_url': 'https://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/8.1.25/xampp-windows-x64-8.1.25-0-VS16-installer.exe', 'file_size': '147 MB'},
                    {'version': '8.0.30 (PHP 8.0)', 'download_url': 'https://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/8.0.30/xampp-windows-x64-8.0.30-0-VS16-installer.exe', 'file_size': '143 MB'}
                ]
            },
            {
                'name': 'Microsoft Visual Studio',
                'slug': 'visualstudio',
                'version': '2022 Community',
                'description': 'Môi trường phát triển tích hợp (IDE) toàn diện, chuyên nghiệp nhất từ Microsoft.',
                'detail_description': 'Microsoft Visual Studio (màu tím đặc trưng) là IDE cực kỳ mạnh mẽ dành cho phát triển các ứng dụng Windows (.NET, C++), web, đám mây và mobile. Thích hợp cho các dự án doanh nghiệp lớn từ Microsoft.',
                'category': 'dev',
                'developer': 'Microsoft Corporation',
                'file_size': '3.5 MB',
                'download_count': 53400,
                'icon_type': 'visualstudio',
                'download_filename': 'vs_community.exe',
                'download_url': 'https://aka.ms/vs/17/release/vs_community.exe',
                'versions': [
                    {'version': '2022 Community (Free)', 'download_url': 'https://aka.ms/vs/17/release/vs_community.exe', 'file_size': '3.5 MB'},
                    {'version': '2022 Professional', 'download_url': 'https://aka.ms/vs/17/release/vs_professional.exe', 'file_size': '3.5 MB'},
                    {'version': '2022 Enterprise', 'download_url': 'https://aka.ms/vs/17/release/vs_enterprise.exe', 'file_size': '3.5 MB'}
                ]
            },
            {
                'name': 'Cursor AI Editor',
                'slug': 'cursor-editor',
                'version': '0.45.8',
                'description': 'Trình biên tập mã nguồn tích hợp AI tiên tiến nhất hiện nay, xây dựng trên VS Code.',
                'detail_description': 'Cursor là IDE lập trình AI thế hệ mới được tối ưu hóa sâu sắc giúp lập trình viên viết code nhanh hơn gấp nhiều lần. Hỗ trợ tự động hoàn thành thông minh, sửa lỗi, giải thích code và chat trực tiếp với các mô hình AI tiên tiến như Claude 3.5 Sonnet, GPT-4o.',
                'category': 'dev',
                'developer': 'Anysphere Inc.',
                'file_size': '124 MB',
                'download_count': 84200,
                'icon_type': 'cursor',
                'download_filename': 'CursorSetup.exe',
                'download_url': 'https://www.cursor.com/api/download?platform=win32-x64&releaseTrack=stable',
                'versions': [
                    {'version': '0.45.8 Stable (64-bit)', 'download_url': 'https://www.cursor.com/api/download?platform=win32-x64&releaseTrack=stable', 'file_size': '124 MB'},
                    {'version': '0.45.0 Stable (64-bit)', 'download_url': 'https://www.cursor.com/api/download?platform=win32-x64&releaseTrack=stable', 'file_size': '123 MB'}
                ]
            },
            {
                'name': 'Docker Desktop',
                'slug': 'docker',
                'version': '4.27.2',
                'description': 'Công cụ đóng gói, quản lý và chạy ứng dụng trong các container tách biệt.',
                'detail_description': 'Docker Desktop cung cấp môi trường hoàn chỉnh để xây dựng, chia sẻ và chạy các ứng dụng container hóa trên Windows. Tích hợp sẵn Kubernetes, Docker Engine và giao diện GUI trực quan.',
                'category': 'dev',
                'developer': 'Docker Inc.',
                'file_size': '584 MB',
                'download_count': 32600,
                'icon_type': 'docker',
                'download_filename': 'Docker-Desktop-Installer.exe',
                'download_url': 'https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe',
                'versions': []
            },
            {
                'name': 'Node.js Runtime',
                'slug': 'nodejs',
                'version': '20.11.1 LTS',
                'description': 'Môi trường chạy mã JavaScript phía máy chủ (Runtime) xây dựng trên V8 engine.',
                'detail_description': 'Node.js cho phép lập trình viên chạy mã JavaScript ngoài trình duyệt để xây dựng các ứng dụng mạng tốc độ cao, API server, và các ứng dụng realtime.',
                'category': 'dev',
                'developer': 'OpenJS Foundation',
                'file_size': '30.1 MB',
                'download_count': 51200,
                'icon_type': 'nodejs',
                'download_filename': 'node-v20.11.1-x64.msi',
                'download_url': 'https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi',
                'versions': [
                    {'version': '20.11.1 LTS', 'download_url': 'https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi', 'file_size': '30.1 MB'},
                    {'version': '21.6.2 Current', 'download_url': 'https://nodejs.org/dist/v21.6.2/node-v21.6.2-x64.msi', 'file_size': '30.4 MB'},
                    {'version': '18.19.1 LTS', 'download_url': 'https://nodejs.org/dist/v18.19.1/node-v18.19.1-x64.msi', 'file_size': '29.8 MB'}
                ]
            },
            {
                'name': 'IntelliJ IDEA Community',
                'slug': 'intellij',
                'version': '2023.3.4',
                'description': 'IDE lập trình Java, Kotlin và phát triển phần mềm doanh nghiệp hàng đầu.',
                'detail_description': 'IntelliJ IDEA là môi trường phát triển tích hợp (IDE) thông minh nhất dành cho Java và Kotlin. Hỗ trợ tái cấu trúc mã nguồn (refactoring), phân tích cú pháp thông minh và tích hợp sẵn các công cụ build phổ biến như Maven, Gradle.',
                'category': 'dev',
                'developer': 'JetBrains s.r.o.',
                'file_size': '672 MB',
                'download_count': 28900,
                'icon_type': 'intellij',
                'download_filename': 'ideaIC-2023.3.4.exe',
                'download_url': 'https://download.jetbrains.com/idea/ideaIC-2023.3.4.exe',
                'versions': [
                    {'version': '2023.3.4 (Community)', 'download_url': 'https://download.jetbrains.com/idea/ideaIC-2023.3.4.exe', 'file_size': '672 MB'},
                    {'version': '2023.2.5 (Community)', 'download_url': 'https://download.jetbrains.com/idea/ideaIC-2023.2.5.exe', 'file_size': '664 MB'}
                ]
            },
            {
                'name': 'Antigravity AI Agent',
                'slug': 'antigravity-agent',
                'version': '2.0.4 Pro',
                'description': 'Trình lập trình viên AI Agent tự động hóa tối tân nhất thế giới, tối ưu hóa code và sửa lỗi 1-Click.',
                'detail_description': 'Antigravity AI Agent là hệ thống lập trình tự động hóa thế hệ mới phát triển bởi Google DeepMind. Agent có khả năng tự tìm hiểu codebase, chỉnh sửa file phức tạp, sửa lỗi biên dịch, và thiết kế UI/UX đỉnh cao theo chuẩn công nghiệp chỉ với một prompt tiếng Việt.',
                'category': 'dev',
                'developer': 'Google DeepMind & Antigravity Team',
                'file_size': '218 MB',
                'download_count': 999999,
                'icon_type': 'antigravity',
                'download_filename': 'Antigravity IDE.exe',
                'download_url': 'https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/2.0.4-6381998290370560/windows-x64/Antigravity%20IDE.exe',
                'versions': [
                    {'version': '2.0.4 Pro (Agentic AI)', 'download_url': 'https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/2.0.4-6381998290370560/windows-x64/Antigravity%20IDE.exe', 'file_size': '218 MB'},
                    {'version': '1.23.2 Stable (Agentic AI)', 'download_url': 'https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/1.23.2-4781536860569600/windows-x64/Antigravity.exe', 'file_size': '208 MB'}
                ]
            },
            
            # Đồ họa & Thiết kế (design)
            {
                'name': 'Blender 3D',
                'slug': 'blender',
                'version': '4.0.2',
                'description': 'Phần mềm thiết kế đồ họa 3D, dựng hoạt hình và biên tập video mã nguồn mở.',
                'detail_description': 'Blender là bộ công cụ sáng tạo nội dung 3D hoàn toàn miễn phí và mã nguồn mở. Nó hỗ trợ toàn bộ quy trình dựng hình: mô hình hóa (modeling), dựng xương (rigging), hoạt họa (animation), mô phỏng vật lý, render và hậu kỳ video.',
                'category': 'design',
                'developer': 'Blender Foundation',
                'file_size': '312 MB',
                'download_count': 29400,
                'icon_type': 'blender',
                'download_filename': 'blender-4.0.2-windows-x64.msi',
                'download_url': 'https://download.blender.org/release/Blender4.0/blender-4.0.2-windows-x64.msi',
                'versions': []
            },
            {
                'name': 'GIMP Image Editor',
                'slug': 'gimp',
                'version': '2.10.36',
                'description': 'Phần mềm chỉnh sửa ảnh chuyên nghiệp, giải pháp thay thế Photoshop miễn phí.',
                'detail_description': 'GIMP (GNU Image Manipulation Program) là trình chỉnh sửa đồ họa raster miễn phí. Nó được dùng cho việc chỉnh sửa ảnh, vẽ tự do, chuyển đổi định dạng ảnh và các tác vụ chuyên biệt tương đương Adobe Photoshop.',
                'category': 'design',
                'developer': 'GIMP Development Team',
                'file_size': '301 MB',
                'download_count': 18700,
                'icon_type': 'gimp',
                'download_filename': 'gimp-2.10.36-setup.exe',
                'download_url': 'https://download.gimp.org/gimp/v2.10/windows/gimp-2.10.36-setup.exe',
                'versions': []
            },
            
            # Tiện ích (utilities)
            {
                'name': 'VLC Media Player',
                'slug': 'vlc',
                'version': '3.0.20',
                'description': 'Trình phát đa phương tiện miễn phí, mở được hầu hết mọi định dạng video và nhạc.',
                'detail_description': 'VLC Media Player là trình phát đa phương tiện đa nền tảng miễn phí, mã nguồn mở. Nó có thể chơi hầu hết các tệp đa phương tiện cũng như đĩa DVD, Audio CD, VCD và các giao thức phát sóng trực tiếp mà không cần cài thêm bộ giải mã (codecs).',
                'category': 'utilities',
                'developer': 'VideoLAN Association',
                'file_size': '42.3 MB',
                'download_count': 82100,
                'icon_type': 'vlc',
                'download_filename': 'vlc-3.0.20-win64.exe',
                'download_url': 'https://get.videolan.org/vlc/3.0.20/win64/vlc-3.0.20-win64.exe',
                'versions': []
            },
            {
                'name': 'WinRAR Archiver',
                'slug': 'winrar',
                'version': '6.24',
                'description': 'Phần mềm nén và giải nén tệp tin RAR, ZIP mạnh mẽ hàng đầu thế giới.',
                'detail_description': 'WinRAR là một công cụ lưu trữ cực mạnh giúp nén và giải nén dữ liệu nhanh chóng. Nó có thể sao lưu dữ liệu của bạn, giảm kích thước các tệp đính kèm email, giải nén các tệp RAR, ZIP và các tệp khác được tải xuống từ Internet.',
                'category': 'utilities',
                'developer': 'RARLAB',
                'file_size': '3.6 MB',
                'download_count': 156400,
                'icon_type': 'winrar',
                'download_filename': 'winrar-x64-624.exe',
                'download_url': 'https://www.rarlab.com/rar/winrar-x64-624.exe',
                'versions': []
            },
            {
                'name': 'CCleaner Utility',
                'slug': 'ccleaner',
                'version': '6.20',
                'description': 'Tiện ích dọn rác hệ thống, sửa lỗi registry và tối ưu tốc độ máy tính.',
                'detail_description': 'CCleaner là công cụ dọn dẹp hàng đầu giúp bảo vệ sự riêng tư và giúp máy tính hoạt động nhanh hơn, an toàn hơn. Phần mềm sẽ xóa bỏ các tệp rác, lịch sử duyệt web và các tệp tin tạm thời giải phóng không gian ổ cứng.',
                'category': 'utilities',
                'developer': 'Piriform Software',
                'file_size': '34.5 MB',
                'download_count': 73200,
                'icon_type': 'ccleaner',
                'download_filename': 'ccsetup620.exe',
                'download_url': 'https://download.ccleaner.com/ccsetup620.exe',
                'versions': []
            },
            {
                'name': 'VMware Workstation Pro',
                'slug': 'vmware',
                'version': '17.5.2',
                'description': 'Phần mềm ảo hóa máy tính mạnh mẽ nhất, chạy nhiều hệ điều hành cùng lúc.',
                'detail_description': 'VMware Workstation cho phép các chuyên gia công nghệ thông tin và lập trình viên chạy nhiều máy ảo trên cùng một hệ điều hành Windows. Tạo môi trường độc lập thử nghiệm ứng dụng an toàn.',
                'category': 'utilities',
                'developer': 'VMware (Broadcom)',
                'file_size': '618 MB',
                'download_count': 26400,
                'icon_type': 'vmware',
                'download_filename': 'VMware-workstation-full-17.5.2-23775571.exe',
                'download_url': 'https://archive.org/download/vmwareworkstationarchive/17.x/VMware-workstation-full-17.5.2-23775571.exe',
                'versions': [
                    {'version': '17.5.2 (Win 64-bit)', 'download_url': 'https://archive.org/download/vmwareworkstationarchive/17.x/VMware-workstation-full-17.5.2-23775571.exe', 'file_size': '618 MB'},
                    {'version': '17.0.2 (Win 64-bit)', 'download_url': 'https://archive.org/download/vmwareworkstationarchive/17.x/VMware-workstation-full-17.0.2-21581411.exe', 'file_size': '608 MB'}
                ]
            },
            {
                'name': 'Oracle VM VirtualBox',
                'slug': 'virtualbox',
                'version': '7.0.14',
                'description': 'Phần mềm ảo hóa mã nguồn mở miễn phí, hỗ trợ giả lập nhiều hệ điều hành trên máy tính.',
                'detail_description': 'Oracle VM VirtualBox là phần mềm ảo hóa miễn phí và mã nguồn mở mạnh mẽ, cho phép người dùng chạy thử nghiệm các hệ điều hành khác (Linux, Windows, macOS...) ngay trên máy tính hiện tại mà không làm ảnh hưởng đến hệ thống chính.',
                'category': 'utilities',
                'developer': 'Oracle Corporation',
                'file_size': '106 MB',
                'download_count': 32700,
                'icon_type': 'virtualbox',
                'download_filename': 'VirtualBox-7.0.14-161095-Win.exe',
                'download_url': 'https://download.virtualbox.org/virtualbox/7.0.14/VirtualBox-7.0.14-161095-Win.exe',
                'versions': [
                    {'version': '7.0.14 (Win 64-bit)', 'download_url': 'https://download.virtualbox.org/virtualbox/7.0.14/VirtualBox-7.0.14-161095-Win.exe', 'file_size': '106 MB'},
                    {'version': '6.1.50 (Win 64-bit)', 'download_url': 'https://download.virtualbox.org/virtualbox/6.1.50/VirtualBox-6.1.50-161033-Win.exe', 'file_size': '103 MB'}
                ]
            },
            
            # Trò chơi & Kết nối (games)
            {
                'name': 'Steam Client',
                'slug': 'steam',
                'version': '1.0.0.79',
                'description': 'Nền tảng phân phối game bản quyền trực tuyến lớn nhất thế giới.',
                'detail_description': 'Steam là điểm đến tối thượng để chơi game, thảo luận và sáng tạo trò chơi. Với hàng chục ngàn tựa game bản quyền đa dạng, cập nhật tự động và cộng đồng người chơi sôi động toàn cầu.',
                'category': 'games',
                'developer': 'Valve Corporation',
                'file_size': '2.1 MB',
                'download_count': 112500,
                'icon_type': 'steam',
                'download_filename': 'SteamSetup.exe',
                'download_url': 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe',
                'versions': []
            },
            {
                'name': 'Discord Chat',
                'slug': 'discord',
                'version': '1.0.9030',
                'description': 'Ứng dụng liên lạc thoại, gọi video và trò chuyện văn bản dành cho game thủ.',
                'detail_description': 'Discord là cách dễ nhất để nói chuyện qua giọng nói, video và văn bản. Phần mềm cho phép bạn tạo lập các kênh chat riêng tư, chia sẻ màn hình chơi game mượt mà với bạn bè hoàn toàn miễn phí.',
                'category': 'games',
                'developer': 'Discord Inc.',
                'file_size': '85.6 MB',
                'download_count': 94500,
                'icon_type': 'discord',
                'download_filename': 'DiscordSetup.exe',
                'download_url': 'https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86',
                'versions': []
            },
            
            # Văn phòng & Liên lạc (office)
            {
                'name': 'TeamViewer Remote',
                'slug': 'teamviewer',
                'version': '15.51.5',
                'description': 'Giải pháp kết nối máy tính và hỗ trợ điều khiển từ xa số một thế giới.',
                'detail_description': 'TeamViewer giúp bạn kết nối và kiểm soát màn hình máy tính từ xa ở bất cứ đâu. Hỗ trợ truyền tập tin và chat trực tuyến vô cùng tiện lợi cho công việc văn phòng và kỹ thuật.',
                'category': 'office',
                'developer': 'TeamViewer US LLC',
                'file_size': '74.8 MB',
                'download_count': 49200,
                'icon_type': 'teamviewer',
                'download_filename': 'TeamViewer_Setup_x64.exe',
                'download_url': 'https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe',
                'versions': []
            },
            {
                'name': 'UltraViewer Control',
                'slug': 'ultraviewer',
                'version': '6.6',
                'description': 'Phần mềm điều khiển máy tính từ xa siêu nhẹ, miễn phí và phổ biến tại Việt Nam.',
                'detail_description': 'UltraViewer giúp bạn điều khiển máy khách từ xa để hỗ trợ phần mềm nhanh chóng. Giao diện đơn giản, an toàn tuyệt đối với cơ chế sinh mật khẩu ngẫu nhiên cho mỗi phiên làm việc.',
                'category': 'office',
                'developer': 'UltraViewer Co., Ltd',
                'file_size': '3.5 MB',
                'download_count': 61200,
                'icon_type': 'ultraviewer',
                'download_filename': 'UltraViewer_setup_6.6_vi.exe',
                'download_url': 'https://ultraviewer.net/vi/UltraViewer_setup_6.6_vi.exe',
                'versions': []
            },
            
            # Bảo mật (security)
            {
                'name': 'Malwarebytes Security',
                'slug': 'malwarebytes',
                'version': '4.6.8',
                'description': 'Phần mềm quét và loại bỏ phần mềm độc hại, trojan và ransomware mạnh mẽ.',
                'detail_description': 'Malwarebytes là phần mềm diệt virus và mã độc thế hệ mới, bảo vệ máy tính của bạn trước các phần mềm gián điệp, phần mềm quảng cáo độc hại và tin tặc bằng hệ thống phát hiện hành vi thời gian thực thông minh.',
                'category': 'security',
                'developer': 'Malwarebytes Inc.',
                'file_size': '2.8 MB',
                'download_count': 34500,
                'icon_type': 'malwarebytes',
                'download_filename': 'MBSetup.exe',
                'download_url': 'https://downloads.malwarebytes.com/file/mb-windows',
                'versions': []
            },
            
            # Văn phòng & Tiện ích văn phòng (office)
            {
                'name': 'Notepad++',
                'slug': 'notepadpp',
                'version': '8.6.2',
                'description': 'Trình soạn thảo văn bản và mã nguồn đa năng, siêu nhẹ cho Windows.',
                'detail_description': 'Notepad++ là trình soạn thảo văn bản miễn phí thay thế hoàn hảo cho Notepad của Windows. Nó hỗ trợ bôi màu cú pháp cho nhiều ngôn ngữ lập trình, mở nhiều tab cùng lúc và có dung lượng cực kỳ gọn nhẹ.',
                'category': 'office',
                'developer': 'Don Ho',
                'file_size': '4.5 MB',
                'download_count': 67400,
                'icon_type': 'notepadpp',
                'download_filename': 'npp.8.6.2.Installer.x64.exe',
                'download_url': 'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6.2/npp.8.6.2.Installer.x64.exe',
                'versions': []
            },
            {
                'name': 'UniKey Keyboard',
                'slug': 'unikey',
                'version': '4.3 RC4',
                'description': 'Bộ gõ tiếng Việt tốt nhất, gọn nhẹ và phổ biến nhất trên hệ điều hành Windows.',
                'detail_description': 'UniKey là chương trình gõ tiếng Việt mã nguồn mở miễn phí phổ biến nhất tại Việt Nam. Nó hỗ trợ các bảng mã tiếng Việt thông dụng (Unicode, VNI, TCVN3...) và kiểu gõ Telex, VNI rất chuẩn xác.',
                'category': 'office',
                'developer': 'Pham Kim Long',
                'file_size': '0.8 MB',
                'download_count': 189500,
                'icon_type': 'unikey',
                'download_filename': 'unikey43RC4-180714-win64.zip',
                'download_url': 'https://downloads.sourceforge.net/project/unikey/unikey-win/4.3%20RC4/unikey43RC4-180714-win64.zip',
                'versions': [
                    {'version': '4.3 RC4 (Win 64-bit)', 'download_url': 'https://downloads.sourceforge.net/project/unikey/unikey-win/4.3%20RC4/unikey43RC4-180714-win64.zip', 'file_size': '0.8 MB'},
                    {'version': '4.2 RC4 (Win 64-bit)', 'download_url': 'https://downloads.sourceforge.net/project/unikey/unikey-win/4.2%20RC4/unikey42RC4-140823-win64.zip', 'file_size': '0.7 MB'}
                ]
            },
            {
                'name': 'Zoom Meetings',
                'slug': 'zoom',
                'version': '5.17.5',
                'description': 'Ứng dụng tổ chức hội thảo, học tập và họp trực tuyến hàng đầu.',
                'detail_description': 'Zoom Meetings cung cấp giải pháp họp trực tuyến, hội nghị truyền hình chất lượng HD sắc nét, chia sẻ tài liệu tiện lợi hỗ trợ làm việc và học tập từ xa dễ dàng.',
                'category': 'office',
                'developer': 'Zoom Video Communications',
                'file_size': '82.3 MB',
                'download_count': 51200,
                'icon_type': 'zoom',
                'download_filename': 'ZoomInstaller.exe',
                'download_url': 'https://zoom.us/client/latest/ZoomInstaller.exe',
                'versions': []
            },
            
            # Hệ điều hành & ISO (os_iso)
            {
                'name': 'Microsoft Windows 11',
                'slug': 'windows-11',
                'version': '23H2',
                'description': 'File ISO cài đặt hệ điều hành Windows 11 Enterprise chính thức của Microsoft.',
                'detail_description': 'Bản cài đặt ISO chính thức của Windows 11 Enterprise (23H2) nguyên bản, tích hợp sẵn các tính năng bảo mật nâng cao, Copilot AI và giao diện thiết kế bo góc vô cùng hiện đại.',
                'category': 'os_iso',
                'developer': 'Microsoft Corporation',
                'file_size': '6.2 GB',
                'download_count': 89400,
                'icon_type': 'windows',
                'download_filename': 'Win11_23H2_English_x64.iso',
                'download_url': 'https://archive.org/download/win-11-23h2/Win11_23H2_English_x64.iso',
                'versions': [
                    {'version': '23H2 (Win 64-bit)', 'download_url': 'https://archive.org/download/win-11-23h2/Win11_23H2_English_x64.iso', 'file_size': '6.2 GB'},
                    {'version': '22H2 (Win 64-bit)', 'download_url': 'https://archive.org/download/windows-11-version-22h2/Win11_22H2_English_x64.iso', 'file_size': '5.5 GB'}
                ]
            },
            {
                'name': 'Microsoft Windows 10',
                'slug': 'windows-10',
                'version': '22H2',
                'description': 'File ISO cài đặt hệ điều hành Windows 10 Enterprise ổn định và phổ biến nhất.',
                'detail_description': 'Bản cài đặt ISO chính thức của Windows 10 Enterprise (22H2) nguyên bản. Hoàn hảo cho mọi máy tính cá nhân và doanh nghiệp với hiệu năng tối ưu, tính tương thích phần mềm tốt nhất.',
                'category': 'os_iso',
                'developer': 'Microsoft Corporation',
                'file_size': '5.7 GB',
                'download_count': 124300,
                'icon_type': 'windows',
                'download_filename': 'Win10_22H2_English_x64.iso',
                'download_url': 'https://archive.org/download/win-10-22-h-2-english-x-64_202308/Win10_22H2_English_x64.iso',
                'versions': [
                    {'version': '22H2 (Win 64-bit)', 'download_url': 'https://archive.org/download/win-10-22-h-2-english-x-64_202308/Win10_22H2_English_x64.iso', 'file_size': '5.7 GB'},
                    {'version': '21H2 (Win 64-bit)', 'download_url': 'https://archive.org/download/windows-10-english-21h2/Win10_21H2_English_x64.iso', 'file_size': '5.5 GB'}
                ]
            },
            {
                'name': 'Microsoft Windows 7',
                'slug': 'windows-7',
                'version': 'SP1 Ultimate',
                'description': 'File ISO cài đặt hệ điều hành Windows 7 Ultimate SP1 64-bit huyền thoại.',
                'detail_description': 'Hệ điều hành Windows 7 SP1 Ultimate 64-bit/32-bit nguyên bản sạch, cực kỳ nhẹ nhàng và ổn định. Là lựa chọn tuyệt vời cho các dòng máy cấu hình cũ hoặc cài đặt làm máy ảo thử nghiệm.',
                'category': 'os_iso',
                'developer': 'Microsoft Corporation',
                'file_size': '3.1 GB',
                'download_count': 43600,
                'icon_type': 'windows',
                'download_filename': 'en_windows_7_ultimate_with_sp1_x64_dvd_u_677332.iso',
                'download_url': 'https://archive.org/download/Windows-7-Collection/en_windows_7_ultimate_with_sp1_x64_dvd_u_677332.iso',
                'versions': [
                    {'version': 'SP1 Ultimate (64-bit)', 'download_url': 'https://archive.org/download/Windows-7-Collection/en_windows_7_ultimate_with_sp1_x64_dvd_u_677332.iso', 'file_size': '3.1 GB'},
                    {'version': 'SP1 Ultimate (32-bit)', 'download_url': 'https://archive.org/download/Windows-7-Collection/en_windows_7_ultimate_with_sp1_x86_dvd_u_677460.iso', 'file_size': '2.4 GB'}
                ]
            },
            {
                'name': 'Ubuntu Desktop',
                'slug': 'ubuntu',
                'version': '24.04.4 LTS',
                'description': 'Hệ điều hành mã nguồn mở Linux phổ biến và thân thiện nhất hiện nay.',
                'detail_description': 'Ubuntu Desktop 24.04.4 LTS (Noble Numbat) đem lại môi trường làm việc trực quan, hiện đại, tích hợp sẵn trình duyệt, bộ ứng dụng văn phòng LibreOffice và kho ứng dụng khổng lồ cực kỳ bảo mật.',
                'category': 'os_iso',
                'developer': 'Canonical Ltd.',
                'file_size': '5.7 GB',
                'download_count': 61400,
                'icon_type': 'ubuntu',
                'download_filename': 'ubuntu-24.04.4-desktop-amd64.iso',
                'download_url': 'https://releases.ubuntu.com/24.04/ubuntu-24.04.4-desktop-amd64.iso',
                'versions': [
                    {'version': '24.04.4 LTS (Noble Numbat)', 'download_url': 'https://releases.ubuntu.com/24.04/ubuntu-24.04.4-desktop-amd64.iso', 'file_size': '5.7 GB'},
                    {'version': '22.04.5 LTS (Jammy Jellyfish)', 'download_url': 'https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso', 'file_size': '4.7 GB'}
                ]
            },
            {
                'name': 'Kali Linux Installer',
                'slug': 'kali-linux',
                'version': '2026.1',
                'description': 'Bản phân phối Linux tối thượng cho kiểm thử bảo mật và hack đạo đức.',
                'detail_description': 'Kali Linux là hệ điều hành mã nguồn mở dựa trên Debian, được cấu hình sẵn hàng trăm công cụ chuyên sâu về kiểm thử xâm nhập, phân tích mã độc, phục hồi thông tin và bảo mật mạng.',
                'category': 'os_iso',
                'developer': 'OffSec',
                'file_size': '4.4 GB',
                'download_count': 39800,
                'icon_type': 'kali',
                'download_filename': 'kali-linux-2026.1-installer-amd64.iso',
                'download_url': 'https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso',
                'versions': [
                    {'version': '2026.1 (64-bit)', 'download_url': 'https://cdimage.kali.org/kali-2026.1/kali-linux-2026.1-installer-amd64.iso', 'file_size': '4.4 GB'},
                    {'version': '2025.4 (64-bit)', 'download_url': 'https://cdimage.kali.org/kali-2025.4/kali-linux-2025.4-installer-amd64.iso', 'file_size': '4.1 GB'}
                ]
            }
        ]
        
        for item in software_list:
            sw = Software(
                name=item['name'],
                slug=item['slug'],
                version=item['version'],
                description=item['description'],
                detail_description=item['detail_description'],
                category=item['category'],
                developer=item['developer'],
                file_size=item['file_size'],
                download_count=item['download_count'],
                icon_type=item['icon_type'],
                download_filename=item['download_filename'],
                download_url=item['download_url']
            )
            db.session.add(sw)
            db.session.flush() # Để lấy ID của sw
            
            # Nạp danh sách các phiên bản nếu có
            if item['versions']:
                for ver_item in item['versions']:
                    v = SoftwareVersion(
                        software_id=sw.id,
                        version=ver_item['version'],
                        download_url=ver_item['download_url'],
                        file_size=ver_item['file_size']
                    )
                    db.session.add(v)
            
        db.session.commit()
        print("Đã nạp toàn bộ dữ liệu phần mềm, ứng dụng mới và các phiên bản thành công!")

if __name__ == '__main__':
    seed_database()
