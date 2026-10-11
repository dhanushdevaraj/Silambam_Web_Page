/**
 * Silambam Academy - Interactive JavaScript Functionality
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            const isActive = navMenu.classList.toggle('active');
            mobileToggle.setAttribute('aria-expanded', isActive ? 'true' : 'false');
        });

        // Close mobile menu on link click
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                mobileToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // 2. Navbar Scrolled Background Effect
    const siteHeader = document.getElementById('siteHeader');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            siteHeader?.classList.add('scrolled');
        } else {
            siteHeader?.classList.remove('scrolled');
        }
    });

    // 3. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const questionBtn = item.querySelector('.faq-question');
        if (questionBtn) {
            questionBtn.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                // Close all others
                faqItems.forEach(other => other.classList.remove('active'));
                // Toggle clicked
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // 4. Set Minimum Date on Booking Date Pickers (Today or later)
    const datePickers = document.querySelectorAll('input[type="date"]');
    const today = new Date().toISOString().split('T')[0];
    datePickers.forEach(input => {
        input.setAttribute('min', today);
    });

    // 5. Interactive Tuition Fee Calculator (if on schedule page or section)
    const batchSelect = document.getElementById('calcBatch');
    const cycleSelect = document.getElementById('calcCycle');
    const kitCheckbox = document.getElementById('calcKit');
    const priceDisplay = document.getElementById('calculatedPrice');
    const planBreakdown = document.getElementById('planBreakdown');

    function updateTuitionFee() {
        if (!batchSelect || !priceDisplay) return;

        let baseMonthly = parseInt(batchSelect.value, 10) || 1500;
        let months = parseInt(cycleSelect ? cycleSelect.value : 1, 10) || 1;
        let includeKit = kitCheckbox ? kitCheckbox.checked : false;

        let subtotal = baseMonthly * months;
        let discount = 0;

        // Discounts
        if (months === 3) discount = 0.10; // 10% off quarterly
        if (months === 12) discount = 0.25; // 25% off annual

        let discountedTotal = Math.round(subtotal * (1 - discount));
        let kitCost = includeKit ? 650 : 0;
        let finalAmount = discountedTotal + kitCost;

        priceDisplay.textContent = `₹${finalAmount.toLocaleString('en-IN')}`;

        if (planBreakdown) {
            let discountText = discount > 0 ? ` (${discount * 100}% discount applied)` : '';
            let kitText = includeKit ? ` + ₹650 Starter Bamboo Weapon Kit` : '';
            planBreakdown.textContent = `${months} Month(s) enrollment${discountText}${kitText}`;
        }
    }

    if (batchSelect) {
        batchSelect.addEventListener('change', updateTuitionFee);
        if (cycleSelect) cycleSelect.addEventListener('change', updateTuitionFee);
        if (kitCheckbox) kitCheckbox.addEventListener('change', updateTuitionFee);
        updateTuitionFee();
    }

    // 6. Filter Timetable Rows
    const filterButtons = document.querySelectorAll('.schedule-filter-btn');
    const timetableRows = document.querySelectorAll('.timetable-row');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            timetableRows.forEach(row => {
                if (filterValue === 'all' || row.getAttribute('data-category') === filterValue) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    });
});
